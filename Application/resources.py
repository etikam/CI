from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from .models import Etudiant, Departement, Licence

class EtudiantResource(resources.ModelResource):
   
   
    username = fields.Field(attribute='user__username', column_name='username')
    last_name = fields.Field(attribute='user__last_name', column_name='last_name')
    first_name = fields.Field(attribute='user__first_name', column_name='first_name')
    departement = fields.Field(column_name='departement', attribute='departement',
                               widget=ForeignKeyWidget(Departement, 'id'))
    licence = fields.Field(column_name='licence', attribute='licence',
                           widget=ForeignKeyWidget(Licence, 'id'))
    ine = fields.Field(column_name='ine', attribute='ine')
    pv = fields.Field(column_name='pv', attribute='pv')
    pere = fields.Field(column_name='pere', attribute='pere')
    mere = fields.Field(column_name='mere', attribute='mere')
    date_naissance = fields.Field(column_name='date_naissance', attribute='date_naissance')
    lieu_naissance = fields.Field(column_name='lieu_naissance', attribute='lieu_naissance')
    ecole_origine = fields.Field(column_name='ecole_origine', attribute='ecole_origine')
    homme = fields.Field(column_name='homme', attribute='genre')

    class Meta:
        model = Etudiant
        
        fields = ('username', 'last_name', 'first_name', 'departement', 'licence', 'ine', 'pv',
                  'pere', 'mere', 'date_naissance', 'lieu_naissance', 'ecole_origine', 'homme')

    def before_import_row(self, row, **kwargs):
      
        username = row.get('username')
        print(f"===matricule lu: {username}")
        if username:
            user_obj, created = User.objects.get_or_create(username=username)
            if created:
                # Gérer la création d'un nouveau mot de passe si nécessaire
                user_obj.set_password('CI2023@2024')
                user_obj.save()
            # Assigner l'instance User à l'instance Etudiant
            row['user'] = user_obj.username
            print(f"===Id remi à jour: {user_obj.username}")
    def after_save_instance(self, instance, using_transactions=True, dry_run=False):
        print("===After saving====")
        if hasattr(instance, 'user'):
            user_id = instance.user
            if user_id:
                user_obj = User.objects.get(username=user_id)
                instance.user = user_obj
                instance.save()
