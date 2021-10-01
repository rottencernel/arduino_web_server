import logging
from django.shortcuts import render
from django.http import HttpResponse
from .com_port_utils import command_list

logger = logging.getLogger(__name__)


def start(request):
    logger.info('start')
    return render(request, 'startpage.html')


def home(request):
    return render(request, 'home.html')
