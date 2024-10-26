from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from courses.models import Courses
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CourseDetailView(View):
    def get(self, request, course_id=None):
        if course_id is None:

            courses = list(Courses.objects.values())
            return JsonResponse(courses, safe=False)
        else:

            course = get_object_or_404(Courses, id=course_id)
            data = {
                'id': course.id,
                'name': course.name,
                'description': course.description,
            }
            return JsonResponse(data, status=200)

    def post(self, request):
        data = json.loads(request.body)
        course = Courses.objects.create(
            name=data['name'],
            description=data['description']
        )
        return JsonResponse({'id': course.id, 'name': course.name, 'description': course.description}, status=201)

    def put(self, request, course_id):
        data = json.loads(request.body)
        course = get_object_or_404(Courses, id=course_id)

        errors = {}
        if 'name' in data:
            if not data['name']:
                errors['name'] = "Este campo não pode ser vazio."
            elif Courses.objects.exclude(id=course_id).filter(name=data['name']).exists():
                errors['name'] = "Este curso já está cadastrado."

        if 'description' in data:
            if not data['description']:
                errors['description'] = "Este campo não pode ser vazio."

        if errors:
            return JsonResponse(errors, status=400)

        if 'name' in data:
            course.name = data['name']
        if 'description' in data:
            course.description = data['description']
        
        course.save()

        return JsonResponse({'id': course.id, 'name': course.name, 'description': course.description}, status=200)

    def delete(self, request, course_id):
        course = get_object_or_404(Courses, id=course_id)
        course.delete()
        return JsonResponse({'message': 'Curso deletado com sucesso.'}, status=204)