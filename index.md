## Bienvenue sur le portfolio de projets Datascience de Ghalia

Ce portfolio contient la liste des projets que j'ai réalisés jusqu'à maintenant. Pour accéder à un projet, il suffit de cliquer sur l'un des liens ci-dessous.

### Liste des projets


[Premier projet](https://github.com/Ghalia671/premier_projet.github.io/tree/gh-pages/Defi_1_3_Ghalia.slides.md)

<a href="https://htmlpreview.github.io/?https://github.com/Ghalia671/premier_projet.github.io/tree/gh-pages/Defi_1_3_Ghalia.slides.html">Premier Projet - Lien HTML </a>
title : Premier projet
filename : Defi_1_3_Ghalia.slides.md

{% for page in site.pages %}
    <a href={{ page.filename }}>{{ page.title }}</a>
{% endfor %}
