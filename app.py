from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request
from saspy import SASsession

sas_output_dir = Path('sas_output')
app = Flask(__name__, static_folder=sas_output_dir)
response_contents = {
    'directory': '',
    'directory_list': [],
    'dataset': '',
    'iframe_filename': '',
    'error': '',
}

sas = SASsession()
SAS_COMMANDS = {
    'run proc contents': 'proc contents order=varnum data=temp_lib.%s; run;',
    'run proc freq': 'proc freq nlevels data=temp_lib.%s; tables _CHAR_; run;',
    'run proc means': 'proc means maxdec=2 data=temp_lib.%s;  run;',
}


@app.route('/', methods=['GET', 'POST'])
def handle_root_request():

    global response_contents

    sas_output_dir.mkdir(parents=True, exist_ok=True)

    if request.method == 'POST':
        command = request.form['command'].lower()
        if command == 'reset page':
            response_contents['directory'] = ''
            response_contents['directory_list'] = []
            response_contents['dataset'] = ''
            response_contents['iframe_filename'] = ''
            response_contents['error'] = ''
        elif command == 'submit directory':
            directory = Path(request.form['directory'])
            if directory.exists() and directory != Path('.'):
                response_contents['directory'] = directory
                response_contents['directory_list'] = list(directory.glob('*.sas7bdat'))
                response_contents['error'] = ''
            else:
                response_contents['directory'] = ''
                response_contents['directory_list'] = ''
                response_contents['error'] = 'Directory Choice Is Invalid.'
            response_contents['dataset'] = ''
            response_contents['iframe_filename'] = ''
        else:
            response_contents['dataset'] = Path(request.form.get('dataset', ''))
            dataset_name = response_contents['dataset'].stem
            if dataset_name:
                sas.saslib('temp_lib', path=str(response_contents['directory']))
                sas_output = sas.submit(SAS_COMMANDS[command] % dataset_name)
                iframe_filename = f'results-%s.html' % datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
                with open(sas_output_dir/iframe_filename, 'w') as fp:
                    fp.write(sas_output['LST'])
                response_contents['iframe_filename'] = iframe_filename
                response_contents['error'] = ''
            else:
                response_contents['iframe_filename'] = ''
                response_contents['error'] = 'No Dataset Selected.'

    return render_template('index.html', **response_contents)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
