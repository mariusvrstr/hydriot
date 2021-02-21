

class TriggerManager(object):
    trigger_list = dict()
    
    def register_one(self, trigger_name, trigger):
        self.trigger_list[trigger_name] = trigger
        pass

    def register_available(self):       
        #TODO: Implement 
        pass