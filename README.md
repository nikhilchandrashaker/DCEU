# DCEU Box Office vs. Critics

Analytics project on the 15 theatrical DC Extended Universe films (2013–2023).

**Questions:** Do critic scores predict return on budget? Which films and directors beat the 2× break-even rule of thumb? How did returns trend across the franchise?

**Files**
- `dceu_films.csv` – title, year, director, budget, worldwide gross, Rotten Tomatoes critics %
- `analysis.py` – pandas: gross multiple, correlation, director averages
- `dashboard.html` – interactive Chart.js dashboard (open in a browser)

**Data caveat:** figures are approximate, from memory of commonly reported numbers. Verify against Box Office Mojo / The Numbers and Rotten Tomatoes before publishing. Zack Snyder's Justice League (2021) is excluded (streaming).

**Next steps:** add audience score, CinemaScore, opening weekend, marketing spend, Marvel comparison set.

**Pages:** `dashboard.html` (charts + table), `timeline.html` (hero-colored timeline with click-to-open film details), `actors.html` (actor search), `crew.html` (director, composer, cinematographer search). Data: `dceu_films.csv`, `cast.csv` (main cast, not exhaustive), `crew.csv`. Crew credits are from memory; verify before publishing.
