# sanal-irade-platformu-backend

## Setup Cities - Towns - Districts

Run below command to create all cities, towns and districts in the database of tools app.

```
docker compose run app_sip python manage.py loaddata fixtures/cities_fixture.json
```

## Multi-Language Support i18n

```
locale
├── en
├── es
└── fr
```

Open the shell and run the following command from your project directory to create a .po message file for each language:

`(env)$ django-admin makemessages --all --ignore=env`

You should now have:

```
locale
├── en
│   └── LC_MESSAGES
│       └── django.po
├── es
│   └── LC_MESSAGES
│       └── django.po
└── fr
    └── LC_MESSAGES
        └── django.po
```

Take note of one of the .po message files:

* msgid: represents the translation string as it appears in the source code.
* msgstr: represents the language translation, which is empty by default. You'll have to supply the actual translation
  for any given string. Currently, only the LANGUAGES from our settings.py file have been marked for translation. You
  can edit .po files from your regular code editor; however, it's recommended to use an editor designed specifically for
  .po like Poedit.

Next, let's compile the messages by running the following command:

`(env)$ django-admin compilemessages --ignore=env`

A .mo compiled message file has been generated for each language:

```
locale
├── en
│   └── LC_MESSAGES
│       ├── django.mo
│       └── django.po
├── es
│   └── LC_MESSAGES
│       ├── django.mo
│       └── django.po
└── fr
    └── LC_MESSAGES
        ├── django.mo
        └── django.po
```

Next, create the migrations:

`(env)$ python manage.py makemigrations`

Before proceeding, replace the following line in the newly created migration file:

`bases=(parler.models.TranslatableModelMixin, models.Model),`

With the following one:

`bases = (parler.models.TranslatableModel, models.Model)`
