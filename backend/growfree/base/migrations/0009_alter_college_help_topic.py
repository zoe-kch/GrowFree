# Generated by Django 4.2.4 on 2023-08-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_college_help_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_help',
            name='topic',
            field=models.CharField(choices=[('School_Before_College', 'School_Before_College'), ('Searching_for_Colleges', 'Searching_for_Colleges'), ('Exam_Prep', 'Exam_Prep'), ('College_Application', 'College_Application'), ('Research', 'Research'), ('Mentors', 'Mentors'), ('Extracurriculars', 'Extracurriculars'), ('Navigating_Scholarships', 'Navigating_Scholarships'), ('Financial_Aid', 'Financial_Aid'), ('Sponsors', 'Sponsors'), ('Budgeting', 'Budgeting'), ('Financial_Literacy_Courses', 'Financial_Literacy_Courses'), ('Additional_resources', 'Additional_resources')], max_length=200),
        ),
    ]
