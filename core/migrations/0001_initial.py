# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('school_title', models.CharField(blank=True, max_length=255, null=True)),
                ('type_so', models.CharField(blank=True, max_length=255, null=True)),
                ('type_olymp', models.CharField(blank=True, max_length=255, null=True)),
                ('subject_title', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('wight', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': (('can_load', 'Can load data'), ('can_export', 'Can export data')),
            },
        ),
        migrations.CreateModel(
            name='OOP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('ugn', models.CharField(blank=True, max_length=255, null=True)),
                ('direction', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('form', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('text', models.TextField(blank=True, null=True)),
                ('variant', models.CharField(blank=True, max_length=255, null=True)),
                ('answer_text', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('max_score', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('current_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CurrentProgress')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('weight_current', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('weight_intermediate', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_intermediate', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_current', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_median', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_mode', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_std', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SemestrData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('semestr', models.PositiveIntegerField(blank=True, null=True)),
                ('avg_score', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('avg_score_first', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('repeat_count', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('grounds', models.CharField(blank=True, max_length=255, null=True)),
                ('finance_variant', models.CharField(blank=True, max_length=255, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('course_number', models.PositiveIntegerField(blank=True, null=True)),
                ('enroll_year', models.PositiveIntegerField(blank=True, null=True)),
                ('study_period', models.CharField(blank=True, max_length=255, null=True)),
                ('score_avg', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_median', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_std', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('score_mode', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('oop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.OOP')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('login', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('study_variant', models.CharField(blank=True, max_length=255, null=True)),
                ('is_online', models.NullBooleanField()),
                ('customer', models.CharField(blank=True, max_length=255, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('live_place', models.CharField(blank=True, max_length=255, null=True)),
                ('procrastination_level_1', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_2', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_3', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_4', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_5', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_6', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_7', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_8', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_9', models.PositiveIntegerField(blank=True, null=True)),
                ('procrastination_level_10', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_1', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_2', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_3', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_4', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_5', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_6', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_7', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_8', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_9', models.PositiveIntegerField(blank=True, null=True)),
                ('abilities_level_10', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_1', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_2', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_3', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_4', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_5', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_6', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_7', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_8', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_9', models.PositiveIntegerField(blank=True, null=True)),
                ('motivation_level_10', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_1', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_2', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_3', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_4', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_5', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_6', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_7', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_8', models.PositiveIntegerField(blank=True, null=True)),
                ('involvement_level_9', models.PositiveIntegerField(blank=True, null=True)),
                ('platform', models.CharField(blank=True, max_length=255, null=True)),
                ('has_experience', models.NullBooleanField()),
                ('consequences', models.CharField(blank=True, max_length=255, null=True)),
                ('has_meetings', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentData2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('university', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('direction', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.PositiveIntegerField(blank=True, null=True)),
                ('progress_over_past_year', models.CharField(blank=True, max_length=255, null=True)),
                ('form_of_financing', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('course_title', models.CharField(blank=True, max_length=255, null=True)),
                ('reason_for_course', models.CharField(blank=True, max_length=255, null=True)),
                ('independence_level', models.CharField(blank=True, max_length=255, null=True)),
                ('learning_format', models.CharField(blank=True, max_length=255, null=True)),
                ('process_format', models.CharField(blank=True, max_length=255, null=True)),
                ('final_test_format', models.CharField(blank=True, max_length=255, null=True)),
                ('course_activities', models.CharField(blank=True, max_length=255, null=True)),
                ('course_difficulty', models.CharField(blank=True, max_length=255, null=True)),
                ('course_load', models.CharField(blank=True, max_length=255, null=True)),
                ('content_score', models.CharField(blank=True, max_length=255, null=True)),
                ('content_compliance', models.CharField(blank=True, max_length=255, null=True)),
                ('course_satisfaction', models.CharField(blank=True, max_length=255, null=True)),
                ('elements_satisfaction', models.CharField(blank=True, max_length=255, null=True)),
                ('content_representation', models.CharField(blank=True, max_length=255, null=True)),
                ('course_score_npoed', models.CharField(blank=True, max_length=255, null=True)),
                ('level_before', models.CharField(blank=True, max_length=255, null=True)),
                ('level_after', models.CharField(blank=True, max_length=255, null=True)),
                ('focus_for_certificate', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_time', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('credit_transfer', models.NullBooleanField()),
                ('readiness_for_final_test', models.CharField(blank=True, max_length=255, null=True)),
                ('preferred_format', models.CharField(blank=True, max_length=255, null=True)),
                ('previous_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('import_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Student')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('module_title', models.CharField(blank=True, max_length=255, null=True)),
                ('weeks', models.PositiveIntegerField(blank=True, null=True)),
                ('credits', models.PositiveIntegerField(blank=True, null=True)),
                ('count_intermediate_tests', models.PositiveIntegerField(blank=True, null=True)),
                ('has_esse', models.NullBooleanField()),
                ('start_requirements', models.CharField(blank=True, max_length=255, null=True)),
                ('thematic_scope', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('module_title', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('part_up', models.CharField(blank=True, max_length=255, null=True)),
                ('credits', models.PositiveIntegerField(blank=True, null=True)),
                ('hours', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.CharField(db_index=True, max_length=255)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('education_level', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.PositiveIntegerField(blank=True, null=True)),
                ('experience_in_university', models.PositiveIntegerField(blank=True, null=True)),
                ('teaching_position', models.CharField(blank=True, max_length=255, null=True)),
                ('scientific_position', models.CharField(blank=True, max_length=255, null=True)),
                ('administrative_position', models.CharField(blank=True, max_length=255, null=True)),
                ('teaching_rate', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('experience_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('form_of_control', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_materials', models.CharField(blank=True, max_length=255, null=True)),
                ('feedback', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='studentcoursesubject',
            name='subject_platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubjectPlatform'),
        ),
        migrations.AddField(
            model_name='studentcoursesubject',
            name='subject_up',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubjectUP'),
        ),
        migrations.AddField(
            model_name='studentcoursesubject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='semestrdata',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.AddField(
            model_name='result',
            name='student_course_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.StudentCourseSubject'),
        ),
    ]
