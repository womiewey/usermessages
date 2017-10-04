from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from basicapp.models import Messages
from basicapp.serializers import MessagesSerializer
from basicapp.forms import FormMessage
# Create your views here.


def index(request):
    return render(request,'index.html')

def form_name_view(request):
    form = FormMessage()

    if request.method == "POST":
        form = FormMessage(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error')           
    return render(request,'message.html',{'form':form})

# @csrf_exempt
# def message_list(request):
#     if request.method == 'GET':
#         messages = Messages.objects.all()
#         serializer = MessagesSerializer(messages,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MessagesSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors,status = 400)

# @csrf_exempt
# def message_detail(request,pk):
#     try:
#         messages = Messages.objects.get(pk=pk)
#     except basicapp.DoesNotExist:
#         return HttpResponse(status = 404)

#     if request.method == 'GET':
#         serializer = MessagesSerializer(messages)
#         return JsonRespone(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MessagesSerializer(basicapp,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonRespone(serializer.errors,status=400)
@csrf_exempt
@api_view(['GET','POST'])
def message_list(request):
    if request.method == 'GET':
        messages = Messages.objects.all()
        serializer = MessagesSerializer(messages,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def message_detail(request, pk):
    try:
        messages = Messages.objects.get(pk=pk)
    except Messages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessagesSerializer(messages)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = MessagesSerializer(messages,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        messages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)