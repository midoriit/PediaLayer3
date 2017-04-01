# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PediaLayer
                                 A QGIS plugin
 Create a layer from DBpedia
                             -------------------
        begin                : 2017-03-31
        copyright            : (C) 2017 by Midori IT Office, LLC
        email                : info@midoriit.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PediaLayer class from file PediaLayer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pedia_layer import PediaLayer
    return PediaLayer(iface)
