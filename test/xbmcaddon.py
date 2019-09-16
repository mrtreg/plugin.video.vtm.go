# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmcaddon module, either using stubs or alternative functionality '''

from __future__ import absolute_import, division, print_function, unicode_literals
import json
from xbmc import getLocalizedString
from xbmcextra import addon_settings, global_settings, import_language, read_addon_xml

GLOBAL_SETTINGS = global_settings()
ADDON_SETTINGS = addon_settings()
ADDON_INFO = read_addon_xml('addon.xml')
ADDON_ID = next(iter(ADDON_INFO.values())).get('id')
PO = import_language(language=GLOBAL_SETTINGS.get('locale.language'))


class Addon:
    ''' A reimplementation of the xbmcaddon Addon class '''

    def __init__(self, id=ADDON_ID):  # pylint: disable=redefined-builtin
        ''' A stub constructor for the xbmcaddon Addon class '''
        self.id = id

    def getAddonInfo(self, key):
        ''' A working implementation for the xbmcaddon Addon class getAddonInfo() method '''
        STUB_INFO = dict(id=self.id, name=self.id, version='2.3.4', type='kodi.inputstream', profile='special://userdata')
        return ADDON_INFO.get(self.id, STUB_INFO).get(key)

    @staticmethod
    def getLocalizedString(msgctxt):
        ''' A working implementation for the xbmcaddon Addon class getLocalizedString() method '''
        return getLocalizedString(msgctxt)

    def getSetting(self, key):
        ''' A working implementation for the xbmcaddon Addon class getSetting() method '''
        return ADDON_SETTINGS.get(self.id, ADDON_SETTINGS).get(key, '')

    @staticmethod
    def openSettings():
        ''' A stub implementation for the xbmcaddon Addon class openSettings() method '''

    def setSetting(self, key, value):
        ''' A stub implementation for the xbmcaddon Addon class setSetting() method '''
        if ADDON_SETTINGS.get(self.id):
            ADDON_SETTINGS[self.id][key] = value
        else:
            ADDON_SETTINGS[key] = value
        with open('test/userdata/addon_settings.json', 'w') as fd:
            json.dump(ADDON_SETTINGS, fd, sort_keys=True, indent=4)