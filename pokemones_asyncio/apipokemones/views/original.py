import time
import smtplib

from django.shortcuts import render, reverse

from apipokemones.api.api_original import get_pokemons, get_imagen


EXCEPCIONES_SMTP = (smtplib.SMTPAuthenticationError,
            smtplib.SMTPConnectError,
            smtplib.SMTPDataError,
            smtplib.SMTPException,
            smtplib.SMTPHeloError,
            smtplib.SMTPRecipientsRefused,
            smtplib.SMTPResponseException,
            smtplib.SMTPSenderRefused,
            smtplib.SMTPServerDisconnected)


def pokemon_list(request):
    a = testtls()
    inicio_tiempo = time.time()
    pokemones = get_pokemons()
    pokemones_con_imagen = []
    for pokemon in pokemones:
        pokemones_con_imagen.append(get_imagen(pokemon['url']))
    cantidad = len(pokemones_con_imagen)
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_list.html', {
        'pokemones': pokemones_con_imagen,
        'tiempo_carga': tiempo_carga,
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES ORIGINAL'
    })


def testtls():
    from django.core.mail.message import EmailMessage
    from django.core.mail import get_connection
    asunto = "PRUEBA TLS"
    msg_html = "PRUEBA TLS"
    destinatario = "sender@example.com"
    from random import randint
    email_tmp = {
        'from': 'Notificaciones Wisphub <notificaciones@wisphub.site>',
        'host': '192.168.3.13',
        'pass': '',
        'port': 25,
        'use_ssl': False,
        'use_tls': True,
        'user': ''
    }
    intentos = 0
    correo_enviado = False
    resultado_envio = ""
    reply_to = ["mail@mail.com"]
    from_email = email_tmp.get('from')
    while correo_enviado == False and intentos <=10:
        connection = get_connection(host=email_tmp.get('host'), port=email_tmp.get('port'),
                                    username=email_tmp.get("user"), password=email_tmp.get("pass"),
                                    use_tls=email_tmp.get("use_tls"), use_ssl=email_tmp.get("use_ssl"))
        try:
            connection.open()
            email = EmailMessage(subject=asunto, body=msg_html, from_email=from_email, to=[destinatario],
                                 cc=cc_email, reply_to=reply_to, connection=connection )
            email.content_subtype = "html"
            email.send()
            resultado_log = guardar_log_mensajeria(LogMensajeria.CORREO, path, empresa)
            correo_enviado = True
            connection.close()

        except EXCEPCIONES_SMTP as error:
            resultado_envio = "Error en Servidor de correo: " + str(error)
        except Exception as error:
            resultado_envio = "Otro error correo: " + str(error)
        intentos += 1
    return resultado_envio + " Intentos de envio: " + str(intentos)
