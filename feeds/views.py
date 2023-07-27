from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Feed  # You forgot to import the Model
from .serializers import FeedSerializer


class FeedViewSet(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(
            feeds, many=True
        )  # If queryset has more than one instance, use many=True
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(
            data=request.data
        )  # Create serializer instance with JSON data
        if serializer.is_valid():
            serializer.save()  # Save if valid
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # Return saved object's data with Created status  # Return saved object's data with Created status
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # If not valid, return errors with Bad Request status

    def put(self, request, pk):  # You need to specify which instance to update
        try:
            datas = Model.objects.get(pk=pk)  # Get the instance
        except Model.DoesNotExist:
            return Response(status=404)  # Not found
        serializer = Serializer(
            datas, data=request.data
        )  # Create serializer instance with model instance and new data
        if serializer.is_valid():
            serializer.save()  # Save if valid
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):  # You need to specify which instance to delete
        try:
            datas = Model.objects.get(pk=pk)  # Get the instance
        except Model.DoesNotExist:
            return Response(status=404)  # Not found
        datas.delete()  # Delete instance
        return Response(status=204)  # No Content


"""
Make sure to replace Model and Serializer with the actual model and serializer you are using. Also, note that I added pk argument to put and delete methods which means primary key. You have to include instance's id in your request URL like this: /datas/{id}/.

This code assumes you're using Django and Django Rest Framework. Also, remember that this is a very basic version of these CRUD operations. For more complex cases (e.g. permissions, different serializers for different operations), you might need to adjust this code.
        """

from users.models import User


class UserNameFeeds(APIView):
    def get(self, request, username):
        print("username", username)
        User.objects.get(username=username)
        print("user objects")

        Feed.objects.filter(user_id=user.id)  # user가 작성한 모든 게시물들을 가져와 줘.
        return Response("ok")
