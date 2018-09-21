from django.http import HttpResponse
from django.template.loader import get_template
from core.utils import render_to_pdf  # created in step 4
from django.views.generic import View
from core.models import PlanoDisciplina


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('plano_de_curso.html')
        context = {
            "plano": PlanoDisciplina.objects.all()[0],

        }
        html = template.render(context)

        pdf = render_to_pdf('plano_de_curso.html', context)
        if pdf:
            reponse = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("plano_de_curso")
            content = "inline; filename='%s'" % (filename)

            download = request.GET.get("download")
            if download:
                content = "attachement; filename='%s'" % (filename)
            reponse['Content-Disposition'] = content
            return reponse
        return  HttpResponse("Not Found")