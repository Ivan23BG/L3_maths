# Mathematics Course Materials Repository

## Overview
This repository contains LaTeX source files and compiled materials for various mathematics courses:
- HAX501X: Groups and Rings I (Groupes et Anneaux I)
- HAX502X: Differential Calculus (Calcul différentiel)
- HAX503X: Measure and Integration (Mesure et Intégration)
- HAX506X: Probability Theory (Probabilités)

## Repository Structure
```
.
├── build/          # Build artifacts and intermediate files
├── logs/           # Compilation logs
├── pdfs/           # Generated PDF documents
└── src/            # Source files
    ├── common/     # Shared LaTeX resources
    │   ├── environments/
    │   └── macros/
    └── [course-code]/  # Course-specific materials
        ├── assets/
        ├── cours/      # Lecture notes
        └── tds/        # Practice exercises
```

## Prerequisites
- TeX Live or MiKTeX distribution
- Make (for build automation)
- Git

## Building the Documents
```bash
# Build all documents
make

# Build specific course materials
make 501
make 502
...
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the [LICENSE-NAME] - see the [LICENSE](LICENSE) file for details.

## Authors
- [Ivan Lejeune]

## Acknowledgments
- University of science and letters of Montpellier