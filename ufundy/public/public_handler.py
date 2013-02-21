'''
Created on Feb 21, 2013

@author: stephen
@file: public_handler.py
'''


import logging

import webapp2

from ufundy import basehandler


class HomeHandler(basehandler.BaseHandler):
    '''
    classdocs
    '''

    def get(self):
        
            page_title = 'testapp - The CrowdFunding Portal'
            page_description = 'testapp - The CrowdFunding Portal'

            context = {'page_title': page_title, \
                       'page_description': page_description, \
                       }
            
            self.render_response('public/splash.html', **context)
            