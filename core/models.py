from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.utils import Loader


class OOP(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    ugn = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    form = models.CharField(max_length=255, blank=True, null=True)

    class Mapping:
        name = 'ООП'
        fields = (
            ('ИД_ООП', 'import_id'),
            ('УГН', 'ugn'),
            ('Направление', 'direction'),
            ('Ступень ВО', 'level'),
            ('Форма', 'form'),
        )


class Student(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    oop = models.ForeignKey(OOP)
    grounds = models.CharField(max_length=255, blank=True, null=True)
    finance_variant = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    course_number = models.PositiveIntegerField(blank=True, null=True)
    enroll_year = models.PositiveIntegerField(blank=True, null=True)
    study_period = models.CharField(max_length=255, blank=True, null=True)
    score_avg = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_median = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_std = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_mode = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Mapping:
        name = 'Участник обучения'
        fields = (
            ('ИД_Участ', 'import_id'),
            ('ИД_ООП', 'oop'),
            ('Основание поступления', 'grounds'),
            ('Форма финансирования', 'finance_variant'),
            ('Форм. подразделение', 'unit'),
            ('Номер курса обучения', 'course_number'),
            ('Год поступления', 'enroll_year'),
            ('Срок обучения', 'study_period'),
            ('Средний балл студента', 'score_avg'),
            ('Медиана балла потока', 'score_median'),
            ('Стд. откл. балла потока', 'score_std'),
            ('Мода балла потока', 'score_mode'),
        )


class Activity(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    student = models.ForeignKey(Student)
    type = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    school_title = models.CharField(max_length=255, blank=True, null=True)
    type_so = models.CharField(max_length=255, blank=True, null=True)
    type_olymp = models.CharField(max_length=255, blank=True, null=True)
    subject_title = models.CharField(max_length=255, blank=True, null=True)
    score = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Mapping:
        name = 'Деятельность'
        fields = (
            ('ИД_Деят', 'import_id'),
            ('ИД_Участ', 'student'),
            ('Тип (ВО, СО, Олимпиада, ЕГЭ, Вступ.)', 'type'),
            ('Дата начала', 'start'),
            ('Дата окончания', 'end'),
            ('Название обр.уч./Уровень олимпиады', 'school_title'),
            ('Тип СО', 'type_so'),
            ('Тип Олимпиады', 'type_olymp'),
            ('Название предмета', 'subject_title'),
            ('Оценка (ЕГЭ) или средний бал(ВО, СО)', 'score'),
        )


class SubjectUP(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    module_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    part_up = models.CharField(max_length=255, blank=True, null=True)
    credits = models.PositiveIntegerField(blank=True, null=True)
    hours = models.PositiveIntegerField(blank=True, null=True)

    class Mapping:
        name = 'Дисциплина из УП'
        fields = (
            ('ИД_Дисц_УП', 'import_id'),
            ('Название модуля', 'module_title'),
            ('Название', 'title'),
            ('Часть УП', 'part_up'),
            ('Число з.е.', 'credits'),
            ('Число часов', 'hours'),
        )


class SubjectPlatform(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    module_title = models.CharField(max_length=255, blank=True, null=True)
    weeks = models.PositiveIntegerField(null=True, blank=True)
    credits = models.PositiveIntegerField(blank=True, null=True)
    count_intermediate_tests = models.PositiveIntegerField(blank=True, null=True)
    has_esse = models.NullBooleanField(blank=True, null=True)
    start_requirements = models.CharField(max_length=255, blank=True, null=True)
    thematic_scope = models.CharField(max_length=255, blank=True, null=True)

    class Mapping:
        name = 'Дисциплина с платформы'
        fields = (
            ('ИД_Дисц_платформы', 'import_id'),
            ('Название модуля', 'module_title'),
            ('Количество недель', 'weeks'),
            ('Число з.е.', 'credits'),
            ('Кол-во промежуточных тестирований', 'count_intermediate_tests'),
            ('Наличие эссе заданий', 'has_esse'),
            ('Требования начального уровня', 'start_requirements'),
            ('Тематическая направленность', 'thematic_scope'),
        )


class Teacher(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    education_level = models.CharField(max_length=255, blank=True, null=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    experience_in_university = models.PositiveIntegerField(null=True, blank=True)
    teaching_position = models.CharField(max_length=255, null=True, blank=True)
    scientific_position = models.CharField(max_length=255, null=True, blank=True)
    administrative_position = models.CharField(max_length=255, null=True, blank=True)
    teaching_rate = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    experience_qualification = models.CharField(max_length=255, null=True, blank=True)
    form_of_control = models.CharField(max_length=255, null=True, blank=True)
    additional_materials = models.CharField(max_length=255, null=True, blank=True)
    feedback = models.CharField(max_length=255, null=True, blank=True)

    class Mapping:
        name = 'Опрос преподавателя'
        fields = (
            ('ИД_Преподавателя', 'import_id'),
            ('Пол', 'sex'),
            ('Возраст', 'age'),
            ('Уровень образования или уч.степень', 'education_level'),
            ('Совокупный преподавательский стаж', 'experience'),
            ('Стаж преподавания в ВУЗе', 'experience_in_university'),
            ('Преподавательская должность', 'teaching_position'),
            ('Научная должность', 'scientific_position'),
            ('Административная должность', 'administrative_position'),
            ('Преподавтаельская ставка', 'teaching_rate'),
            ('Опыт повышения квалификации', 'experience_qualification'),
            ('Форма контроля', 'form_of_control'),
            ('Вспомогательные материалы', 'additional_materials'),
            ('Обратная связь', 'feedback'),
        )


class StudentCourseSubject(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    student = models.ForeignKey(Student)
    subject_up = models.ForeignKey(SubjectUP)
    subject_platform = models.ForeignKey(SubjectPlatform)
    teacher = models.ForeignKey(Teacher)
    login = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    study_variant = models.CharField(max_length=255, blank=True, null=True)
    is_online = models.NullBooleanField(null=True, blank=True)
    customer = models.CharField(max_length=255, blank=True, null=True)

    class Mapping:
        name = 'Участн-Курс-Дисциплина'
        fields = (
            ('ИД_Участн_Дисц_Курс', 'import_id'),
            ('ИД_Участ', 'student'),
            ('ИД_Дисц_УП', 'subject_up'),
            ('ИД_Дисц_платформы', 'subject_platform'),
            ('ИД_Преподавателя', 'teacher'),
            ('Логин', 'login'),
            ('ид_пользоват_в курсе', 'user_id'),
            ('Модель обучения', 'study_variant'),
            ('is_online', 'is_online'),
            ('Поставщик', 'customer'),
        )


class Result(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    student_course_subject = models.ForeignKey(StudentCourseSubject)
    weight_current = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    weight_intermediate = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_intermediate = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_current = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_median = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_mode = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score_std = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Mapping:
        name = 'Результаты обучения на курсе'
        fields = (
            ('ИД_Результат', 'import_id'),
            ('ИД_Участн_Дисц_Курс', 'student_course_subject'),
            ('Вес текущей', 'weight_current'),
            ('Вес промежуточной', 'weight_intermediate'),
            ('Балл за промежуточную', 'score_intermediate'),
            ('Балл за текущую', 'score_current'),
            ('Медиана балла потока по дисциплине', 'score_median'),
            ('Мода балла по дисциплине', 'score_mode'),
            ('Стд откл балла по дисциплине', 'score_std'),
        )


class CurrentProgress(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    result = models.ForeignKey(Result)
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    score = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    wight = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Mapping:
        name = 'Текущая успеваемость'
        fields = (
            ('ИД_Мероприятия', 'import_id'),
            ('ИД_Результат', 'result'),
            ('Название мероприятия', 'title'),
            ('Тип(Лекция, Тест)', 'type'),
            ('Время начала', 'start'),
            ('Время окончания', 'end'),
            ('Балл за мероприятие', 'score'),
            ('Вес мероприятия', 'wight'),
        )


class Quiz(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    current_progress = models.ForeignKey(CurrentProgress)
    text = models.TextField(blank=True, null=True)
    variant = models.CharField(max_length=255, blank=True, null=True)
    answer_text = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    max_score = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    score = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Mapping:
        name = 'Задание'
        fields = (
            ('ИД_Задания', 'import_id'),
            ('ИД_Мероприятия', 'current_progress'),
            ('текст задания', 'text'),
            ('вариант', 'variant'),
            ('текстовое значение ответа', 'answer_text'),
            ('метка времени', 'timestamp'),
            ('дата и время выгрузки', 'created'),
            ('максимальный бал за задание', 'max_score'),
            ('бал за задание', 'score'),
        )


class SemestrData(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    student = models.ForeignKey(Student)
    semestr = models.PositiveIntegerField(null=True, blank=True)
    avg_score = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    avg_score_first = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    repeat_count = models.PositiveIntegerField(null=True, blank=True)

    class Mapping:
        name = 'Данные за семестр'
        fields = (
            ('ИД_Дан_Сем', 'import_id'),
            ('ИД_Участ', 'import_id'),
            ('Семестр', 'semestr'),
            ('Средняя оценка', 'avg_score'),
            ('Средняя оценка(по 1ой сдаче)', 'avg_score_first'),
            ('Количество пересдач', 'repeat_count')
        )


class StudentData1(models.Model):
    import_id = models.CharField(max_length=255, db_index=True)
    date = models.DateTimeField(null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    live_place = models.CharField(max_length=255, null=True, blank=True)
    procrastination_level_1 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_2 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_3 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_4 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_5 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_6 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_7 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_8 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_9 = models.PositiveIntegerField(null=True, blank=True)
    procrastination_level_10 = models.PositiveIntegerField(null=True, blank=True)

    abilities_level_1 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_2 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_3 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_4 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_5 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_6 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_7 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_8 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_9 = models.PositiveIntegerField(null=True, blank=True)
    abilities_level_10 = models.PositiveIntegerField(null=True, blank=True)

    motivation_level_1 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_2 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_3 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_4 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_5 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_6 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_7 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_8 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_9 = models.PositiveIntegerField(null=True, blank=True)
    motivation_level_10 = models.PositiveIntegerField(null=True, blank=True)

    involvement_level_1 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_2 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_3 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_4 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_5 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_6 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_7 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_8 = models.PositiveIntegerField(null=True, blank=True)
    involvement_level_9 = models.PositiveIntegerField(null=True, blank=True)

    platform = models.CharField(max_length=255, null=True, blank=True)
    has_experience = models.NullBooleanField(null=True, blank=True)
    consequences = models.CharField(max_length=255, null=True, blank=True)
    has_meetings = models.NullBooleanField(null=True, blank=True)

    class Mapping:
        name = 'Опросник студента подход 1'
        fields = (
            ('ИД_Участ', 'import_id'),
            ('Дата тестирования', 'date'),
            ('Пол', 'sex'),
            ('Возраст', 'age'),
            ('Место проживания', 'live_place'),
            ('Уровень прокрастинации 1', 'procrastination_level_1'),
            ('Уровень прокрастинации 2', 'procrastination_level_2'),
            ('Уровень прокрастинации 3', 'procrastination_level_3'),
            ('Уровень прокрастинации 4', 'procrastination_level_4'),
            ('Уровень прокрастинации 5', 'procrastination_level_5'),
            ('Уровень прокрастинации 6', 'procrastination_level_6'),
            ('Уровень прокрастинации 7', 'procrastination_level_7'),
            ('Уровень прокрастинации 8', 'procrastination_level_8'),
            ('Уровень прокрастинации 9', 'procrastination_level_9'),
            ('Уровень прокрастинации 10', 'procrastination_level_10'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 1', 'abilities_level_1'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 2', 'abilities_level_2'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 3', 'abilities_level_3'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 4', 'abilities_level_4'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 5', 'abilities_level_5'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 6', 'abilities_level_6'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 7', 'abilities_level_7'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 8', 'abilities_level_8'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 9', 'abilities_level_9'),
            ('Уровень сам. рег. обучения и владения метакогн. способностями 10', 'abilities_level_10'),
            ('Учебная мотивация 1', 'motivation_level_1'),
            ('Учебная мотивация 2', 'motivation_level_2'),
            ('Учебная мотивация 3', 'motivation_level_3'),
            ('Учебная мотивация 4', 'motivation_level_4'),
            ('Учебная мотивация 5', 'motivation_level_5'),
            ('Учебная мотивация 6', 'motivation_level_6'),
            ('Учебная мотивация 7', 'motivation_level_7'),
            ('Учебная мотивация 8', 'motivation_level_8'),
            ('Учебная мотивация 9', 'motivation_level_9'),
            ('Учебная мотивация 10', 'motivation_level_10'),
            ('Уровень вовлеченности 1', 'involvement_level_1'),
            ('Уровень вовлеченности 2', 'involvement_level_2'),
            ('Уровень вовлеченности 3', 'involvement_level_3'),
            ('Уровень вовлеченности 4', 'involvement_level_4'),
            ('Уровень вовлеченности 5', 'involvement_level_5'),
            ('Уровень вовлеченности 6', 'involvement_level_6'),
            ('Уровень вовлеченности 7', 'involvement_level_7'),
            ('Уровень вовлеченности 8', 'involvement_level_8'),
            ('Уровень вовлеченности 9', 'involvement_level_9'),
            ('МООС платформа', 'platform'),
            ('Наличие опыта освоения elearning', 'has_experience'),
            ('Последствия не освоения', 'consequences'),
            ('Наличие очных встреч', 'has_meetings'),

        )


class StudentData2(models.Model):
    import_id = models.OneToOneField(Student)
    date = models.DateTimeField(null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    direction = models.CharField(max_length=255, null=True, blank=True)
    course = models.PositiveIntegerField(null=True, blank=True)
    progress_over_past_year = models.CharField(max_length=255, null=True, blank=True)
    form_of_financing = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    course_title = models.CharField(max_length=255, null=True, blank=True)
    reason_for_course = models.CharField(max_length=255, null=True, blank=True)
    independence_level = models.CharField(max_length=255, null=True, blank=True)
    learning_format = models.CharField(max_length=255, null=True, blank=True)
    process_format = models.CharField(max_length=255, null=True, blank=True)
    final_test_format = models.CharField(max_length=255, null=True, blank=True)
    course_activities = models.CharField(max_length=255, null=True, blank=True)
    course_difficulty = models.CharField(max_length=255, null=True, blank=True)
    course_load = models.CharField(max_length=255, null=True, blank=True)
    content_score = models.CharField(max_length=255, null=True, blank=True)
    content_compliance = models.CharField(max_length=255, null=True, blank=True)
    course_satisfaction = models.CharField(max_length=255, null=True, blank=True)
    elements_satisfaction = models.CharField(max_length=255, null=True, blank=True)
    content_representation = models.CharField(max_length=255, null=True, blank=True)
    course_score_npoed = models.CharField(max_length=255, null=True, blank=True)
    level_before = models.CharField(max_length=255, null=True, blank=True)
    level_after = models.CharField(max_length=255, null=True, blank=True)
    focus_for_certificate = models.CharField(max_length=255, null=True, blank=True)
    amount_time = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    credit_transfer = models.NullBooleanField(null=True, blank=True)
    readiness_for_final_test = models.CharField(max_length=255, null=True, blank=True)
    preferred_format = models.CharField(max_length=255, null=True, blank=True)
    previous_experience = models.CharField(max_length=255, null=True, blank=True)

    class Mapping:
        name = 'Опросник студента подход 2'
        fields = (
            ('ИД_Участ', 'import_id'),
            ('Дата тестирования', 'date'),
            ('Университет', 'university'),
            ('Уровень обучения', 'level'),
            ('Направление подготовки', 'direction'),
            ('Курс', 'course'),
            ('Успеваемость за последний год', 'progress_over_past_year'),
            ('Форма финансирования', 'form_of_financing'),
            ('email', 'email'),
            ('Фамилия', 'last_name'),
            ('Имя', 'first_name'),
            ('Отчество', 'middle_name'),
            ('Выбранный курс', 'course_title'),
            ('Причина выбора курса', 'reason_for_course'),
            ('Уровень самостоятельности', 'independence_level'),
            ('Формат обучения', 'learning_format'),
            ('Формат процесса освоения дисц.', 'process_format'),
            ('Формат итоговой аттестации', 'final_test_format'),
            ('Виды активности во время курса', 'course_activities'),
            ('Сложность курса', 'course_difficulty'),
            ('Нагрузка во время курса', 'course_load'),
            ('Оценка контенте курса', 'content_score'),
            ('Соответствие полученной оценки реальны знаниям', 'content_compliance'),
            ('Удовлетворенность всем курсом', 'course_satisfaction'),
            ('Удовлетворенность отдельными элементами курса', 'elements_satisfaction'),
            ('Полнота представленности контента по курсу', 'content_representation'),
            ('Оценка курсов НПОО', 'course_score_npoed'),
            ('Уровень подготовки до начала обучения', 'level_before'),
            ('Уровень подготовки полсе освоения курса', 'level_after'),
            ('Количество времени, затрачиваемого на курс', 'amount_time'),
            ('Нацеленность на получение сертификата', 'focus_for_certificate'),
            ('Перезачет дисциплины', 'credit_transfer'),
            ('Степень готовности к итоговому тесту', 'readiness_for_final_test'),
            ('Предпочтительный формат обучения', 'preferred_format'),
            ('Предыдущий опыт онлайн-обучения', 'previous_experience'),
        )


class DataLoad(models.Model):
    user = models.ForeignKey(get_user_model())
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)

    def parse(self):
        Loader().load(self.user.company.prefix, self.file.path)

    class Meta:
        permissions = (
            ("can_load", "Can load data"),
            ("can_export", "Can export data"),
        )


@receiver(post_save, sender=DataLoad)
def parse_data(instance, *args, **kwargs):
    instance.parse()
