# Generated by Django 5.2.1 on 2025-05-29 14:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizationData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('analyzed_endpoint', models.CharField(max_length=255)),
                ('input_transformed_data', models.JSONField(default=list)),
                ('all_phrases_analysis', models.JSONField(default=list)),
                ('global_frequency_stats', models.JSONField(default=dict)),
                ('global_percentage_stats', models.JSONField(default=dict)),
                ('per_source_stats', models.JSONField(default=dict)),
                ('probabilistic_insights', models.JSONField(blank=True, default=dict, null=True)),
                ('inferential_stats_summary', models.JSONField(blank=True, default=dict, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_visualization_data',
                'ordering': ['-createdAt'],
            },
        ),
    ]
