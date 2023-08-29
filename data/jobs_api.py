import flask
from flask import request
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    only = ['id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
            'is_finished', 'team_leader']
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify({
        'jobs': [item.to_dict(only=only) for item in jobs]
    })


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs_by_id(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    only = ['id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
            'is_finished', 'team_leader']
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify({
        'jobs': jobs.to_dict(only=only)
    })


@blueprint.route('/api/jobs', methods=['POST'])
def add_jobs():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    keys = ['id', 'job', 'work_size', 'collaborators',
            'is_finished', 'team_leader']
    if not all([key in request.json for key in keys]):
        return flask.jsonify({'error': 'Bed request'})
    db_sess = db_session.create_session()
    if db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first():
        return flask.jsonify({'error': 'ID already exist'})
    jobs = Jobs()
    jobs.id = request.json['id']
    jobs.job = request.json['job']
    jobs.work_size = request.json['work_size']
    jobs.collaborators = request.json['collaborators']
    jobs.is_finished = request.json['is_finished']
    jobs.team_leader = request.json['team_leader']
    db_sess.add(jobs)
    db_sess.commit()
    return flask.jsonify({'success': 'ok'})
