from endpoints.endpoint import EndpointHandle


Handler  = EndpointHandle()
Handler.create_service_url()
HandlerHealthCheck = Handler.process_services(Handler.endpoints)

print(HandlerHealthCheck)