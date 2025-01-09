from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from application.models.bnb import Service, Rule


class AddNewBnb(TemplateView):
    template_name = 'application/templates/create-new-bnb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_services'] = [service.name for service in Service.objects.all()]
        context['rules_checkin'] = [rule for rule in Rule.objects.filter(rule_type='checkin')]
        context['rules_checkout'] = [rule for rule in Rule.objects.filter(rule_type='checkout')]
        context['rules_refund'] = [rule for rule in Rule.objects.filter(rule_type='refund')]
        context['rules_secure'] = [rule for rule in Rule.objects.filter(rule_type='secure')]
        return context

    def post(self, request, *args, **kwargs):
        try:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                new_bnb_info = request.POST.get('bnb_info')
                return JsonResponse({'result': True}, status=200)
            else:
                return JsonResponse({'result': False}, status=400)
        except (ValueError, KeyError) as e:
            return JsonResponse({'result': False}, status=400)
