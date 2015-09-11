from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# from django.template import Context
# import cStringIO as StringIO
# import xhtml2pdf as pisa
# from django.http import HttpResponse
# from cgi import escape


def Email(template, context, subject, text_content, from_email, to):
    htmly = get_template(template)
    c = context
    subject = subject
    text_content = text_content
    html_content = htmly.render(c)
    from_email = from_email
    to = to
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html = template.render(context)
#     result = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
