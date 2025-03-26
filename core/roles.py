from rolepermissions.roles import AbstractUserRole

class Enterprise(AbstractUserRole):
    available_permissions = {'view_vacancie': True, 'change_vacancie':True}
    
