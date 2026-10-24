# cure-thermal-ledger

## Français

Rejouer une cuisson avec incertitudes de température et temps manquants.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m cure_thermal_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Intègre une cinétique Arrhenius du premier ordre sur des paliers déclarés, avec températures bornées. Les lacunes ajoutent une dose entre zéro et A×durée, jamais une température inventée.

### Limites

Paramètres matière fournis, énergie dactivation positive et températures Kelvin ; pas de validation chimique, de thermomécanique ni de réglage machine proposé.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Replay curing with temperature uncertainty and missing intervals.

Synthetic data; no network access or secret required.

```sh
python -m cure_thermal_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Integrates caller-declared first-order Arrhenius kinetics over bounded isothermal intervals. Gaps add exposure between zero and A×duration, never an invented temperature.

### Limits

Caller-supplied material parameters, nonnegative activation energy and Kelvin temperatures; no chemical validation, thermomechanics or machine-setting recommendation.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir curado con incertidumbre térmica e intervalos ausentes.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m cure_thermal_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Integra cinética Arrhenius de primer orden declarada en intervalos isotermos acotados. Las lagunas añaden exposición entre cero y A×duración, nunca temperatura inventada.

### Límites

Parámetros de material suministrados, energía de activación no negativa y temperaturas Kelvin; sin validación química, termomecánica ni recomendación de ajustes.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.nist.gov/programs-projects/measurement-science-additive-manufacturing-program
