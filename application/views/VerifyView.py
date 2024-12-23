import json

from django.views.generic import TemplateView
from django.http import HttpResponse
from application.models import verification
from application.models import accounts
class VerifyView(TemplateView):
    template_name = "application/templates/verity.html"

    def verify_code(request):
        if request.method == 'POST':
            user_id = request.POST.get('userId')
            code = request.POST.get('code')
            is_verify = accounts.objects.get(user_id=user_id).is_verify
            if is_verify:
                response_data = {'success': False}
            else:
                try:
                    verify = verification.objects.get(code=code, account=user_id)
                    if verify.is_expired:
                        response_data = {'success': False}
                    else:
                        accounts.is_verify = True
                        accounts.save()

                        response_data = {'success': True}
                except verify.DoesNotExist:
                    response_data = {'success': False}
        return HttpResponse(json.dumps({
            'success': False
        }), content_type ='application/json', status=405)


