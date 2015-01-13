#!/usr/bin/env python
import yaml

class Config(object):
    def __init__(self):
        self.action_cmd = './show_camera.sh {0} "{1}"' # camera id, description
        self.record_cmd = './record_camera.sh {0} "{1}" "{2}"' # camera id, description, filename
        self.descriptions = [
            'Camera 1',
            'Camera 2',
            'Camera 3',
            'Camera 4',
            'Camera 5',
            'Camera 6',
            'Camera 7',
            'Camera 8'
        ]
        self.enabled = [False] * 8
        self.loadFromFile()

    def loadFromFile(self):
        try:
            fc = yaml.load(file('camconfig.yaml','r'))
            self.action_cmd = fc['action_cmd']
            self.record_cmd = fc['record_cmd']
            self.descriptions = fc['descriptions']
            self.enabled = fc['enabled']
        except Exception, e:
            print("Error while reading configuration: {0}".format(str(e)))

    def saveToFile(self):
        try:
            with file('camconfig.yaml', 'w') as fc:
                yaml.dump({
                    'action_cmd': self.action_cmd,
                    'record_cmd': self.record_cmd,
                    'descriptions': self.descriptions,
                    'enabled': self.enabled
                    }, fc)
        except Exception, e:
            print("Error while saving configuration: {0}".format(str(e)))  
