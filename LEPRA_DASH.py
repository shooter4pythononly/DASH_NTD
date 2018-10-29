#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:51:33 2018

@author: shooter
"""

import dash
import dash_core_components as dcc
import dash_html_components as html



token = 'pk.eyJ1Ijoicm9iaW5zdW5ueSIsImEiOiJjam50Nmh3ZW0wcW9zM3BwNmRjcjgyNjJ3In0.BL1Gs2sYSrUkEJ7soat4jg'



app = dash.Dash()



# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})


app.layout = html.Div(
        html.Div([
                html.Div([
                        html.Div([
                                html.H1(children='Ending NTD’s thru women led WASH',className='eight columns',
                                        style={'position': 'relative','padding-top': 20,'padding-left': 20})
                                ]),
                        html.Div([
                                html.Img(src="https://www.iapb.org/wp-content/uploads/PHFI.png_0-400x177.jpg",
                                         className='one columns',
                                         style={'height': '30%','width': '30%','float': 'right','position': 'relative','margin-top': 10,},),
                                html.Img(src="https://www.leprosy.org/wp-content/themes/blankslate/img/logo.png",
                                         className='one columns',
                                         style={'height': '30%','width': '30%','float': 'right','position': 'relative','margin-top': 20,},),
                                html.Img(src="https://allngoindia.files.wordpress.com/2015/04/lepra-society.jpg",
                                         className='one columns',
                                         style={'height': '30%','width': '30%','float': 'right','position': 'relative','margin-top': 10,},)
                                ], className = 'three columns')
                        ], className = 'row')
                ])
        )

if __name__ == '__main__':
    app.run_server(debug=True)