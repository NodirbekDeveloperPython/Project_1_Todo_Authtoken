from django.http import HttpResponseForbidden
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .models import *
from .serializers import *
# Create your views here.

class AllPlansAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        plan = request.data
        serializer  = PlanSerializer(data=plan)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PlanAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan)
        return Response({"Success": serializer.data})

    def put(self, request, pk):
        plan = Plan.objects.get(id=pk)
        serializer= PlanSerializer(plan, data=request.data)
        if serializer.is_valid() and plan.user == request.user:
            serializer.save()
            return Response({"Success": serializer.data})
        return Response({"Errors": serializer.errors})

    def delete(self,request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan)
        if plan.user == request.user:
            plan.delete()
            return Response({"Success deleted": serializer.data})
        else:
            return Response({"Error":"You can't delete the this Plan, Because it's not your own.", "Plan": serializer.data})


class UsersAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": serializer.data})