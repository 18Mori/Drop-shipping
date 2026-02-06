from rest_framework import viewsets
from rest_framework.response import Response
from .models import Submission
from .serializers import SubmissionSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def retrieve(self, request, pk=None):
        submission = self.get_object()
        serializer = self.get_serializer(submission)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        submission = self.get_object()
        submission.delete()
        return Response(status=204)