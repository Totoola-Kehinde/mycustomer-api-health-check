import settings
from controller.handler import HandleService

# Microservice URL
service_url = settings.server_name

class EndpointHandle(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    endpoints = [
        'user/new',
        'user/all',
        'user/:user_id',
        'user/update/:user_id',
        'user/delete/:user_id',
        'transaction/new',
        'transaction/all',
        'transaction/:transaction_id',
        'transaction/update/:transaction_id',
        'transaction/delete/:transaction_id',
        'reminder/:customer_id',
        'reminder/sms/:customer_id',
        'reminder/email/:customer_id',
        'register/customer',
        'login',
        'auth/verify-phone',
        'auth/verify',
        'call',
        'store/new',
        'store/:store_id',
        'store/update/:store_id',
        'store/delete/:store_id',
        'store/all',
        'customer/new',
        'customer/:customer_id',
        'customer/update/:customer_id',
        'customer/delete/:customer_id',
        'complaint/new',
        'complaint/all',
        'complaint/update/:complaint_id',
        'complaint/delete/:complaint_id'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.endpoints)
        while count < total_service_list:
            self.endpoints[count] = service_url + self.endpoints[count]
            count += 1
        return self.endpoints