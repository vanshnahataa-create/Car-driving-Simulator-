APEX DRIVE 3D — Free Roam Prototype

FEATURES
- Free-roam start flow: no Start Race or race countdown.
- Four selectable paint styles: red, yellow, blue, and black.
- Four selectable spawn destinations around the mountain circuit.
- Four camera modes: Chase, Hood, Cockpit, and Orbit.
- Touch steering, gas, brake; keyboard WASD/arrows, Space handbrake, R reset.
- Python Flask server and /health endpoint for Render.

RUN LOCALLY
1. Install Python 3.10+.
2. Run: pip install -r requirements.txt
3. Run: python server.py (for local testing, add app.run at the bottom if desired; Render uses Gunicorn).

RENDER DEPLOYMENT
1. Upload these files to a GitHub repository: index.html, server.py, requirements.txt, render.yaml, README.txt.
2. In Render choose New + > Blueprint and connect that repository.
3. Render reads render.yaml and deploys the service.
4. Test https://YOUR-SERVICE.onrender.com/health; expected JSON: {"status":"ok","app":"APEX DRIVE 3D"}.

NOTES
- Three.js is loaded from jsDelivr CDN, so internet access is required.
- This is a browser-game prototype, not a production AAA simulator. Car selection currently changes paint color; destination selection changes the spawn point in the same mountain-circuit environment. Physics and scenery can be upgraded iteratively.
