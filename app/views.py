from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback, Audio
from .forms import FeedbackForm
from .models import Contact
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import wave
import datetime
import pvleopard
import matplotlib.pyplot as plt
from joblib import load
import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model('app/static/model/mental_health_detection.h5')
    return model

def load_preprocessor():
    v = load('app/static/model/tfidf_vectorizer.jb')
    return v

# Create your views here.
def landing(request):
    audios = Audio.objects.all()
    ctx = {'audios': audios}
    return render(request, 'landing.html', ctx)

def transcribe(audio_path):
    access_key = 'I1PHMQcPQGRNuStI9lx2TuJqLkNlugkHTgZs4lGGVP11FKDlwhGEIg=='
    leopard = pvleopard.create(access_key)
    transcript, words = leopard.process_file(audio_path)
    return transcript, words

def predict(text):
    data = [text]
    model = load_model()
    v = load_preprocessor()
    vect = v.transform(data).toarray()
    print(vect.shape)
    fig = plt.figure(figsize=(20,.5))
    plt.plot(range(15000), vect[0])
    # remove the borders
    plt.gca().set_axis_off()
    plt.savefig('app/static/images/plot.png', bbox_inches='tight', pad_inches=0)
    my_prediction = model.predict(vect)
    my_prediction = my_prediction > 0.5
    return my_prediction[0][0]

def predict_depression(request, id):
    audio = Audio.objects.get(pk=id)
    transcript, _ = transcribe(audio.path)
    result = predict(transcript)
    ctx = {'audio': audio, 'result': result}
    if result == True:
        ctx['message'] = 'You are in depression'
    else:
        ctx['message'] = 'You are not in depression'
    return render(request, 'predict_depression.html', ctx)



def feedback(request):
    feedform = FeedbackForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('rating')
        if len(name) > 0 and len(email) > 0 and len(message) > 0:
            feed = Feedback(name=name, email=email, message=message, rating=rating)
            feed.save()
            print('Feedback saved')
    ctx = {'form':feedform}
    return render(request, 'feedback.html', ctx)


def contact(request):
    contform = ContactForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        
        if len(name) > 0 and len(email) > 0 and len(subject) > 0:
            cont = Contact(name=name, email=email, subject=subject, mobile=mobile)
            cont.save()
            print('saved')
    ctx = {'form':contform}
    return render(request, 'contact.html', ctx)

def record(request):
    return render(request, 'record.html')

@csrf_exempt
@login_required
def save_audio(request):
    save_path='media/recordings/'
    current_time = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S_")
    file_name = save_path + current_time + 'audio.wav'
    if request.method == 'POST':
        audio_data = request.FILES['audio_data']
        print(audio_data)
        with open(file_name, 'wb+') as destination:
            for chunk in audio_data.chunks():
                destination.write(chunk)
        # save to model
        audio = Audio(path=file_name, user=request.user)
        audio.save()
        return JsonResponse({'status': 'success'})
        

