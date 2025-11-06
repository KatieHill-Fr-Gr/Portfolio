from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    contributors = models.ManyToManyField(
        to='users.User',
        related_name='contributed_projects',
        blank=True
    )
    technologies = models.ManyToManyField(
        to='technologies.Technology',
        related_name='projects'
    )
    date_completed = models.DateField(
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)
    caption = models.CharField(max_length=200, blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', 'uploaded_at']

    def __str__(self):
        return f'Image for {self.project.name}'

class ProjectLink(models.Model):
    LINK_TYPES = [
        ('live', 'Live Site'),
        ('github', 'GitHub Repository')
    ]
    
    project = models.ForeignKey(
        Project,
        related_name='links',
        on_delete=models.CASCADE
    )
    url = models.URLField(max_length=500)
    link_type = models.CharField(max_length=20, choices=LINK_TYPES)
    label = models.CharField(max_length=100, blank=True)
    
    class Meta:
        unique_together = [['project', 'link_type']] # This ensures that a project can only have one url for each link_type (you can't have multiple "GitHub" links for one project)
    
    def __str__(self):
        return f'{self.project.name} - {self.get_link_type_display()}'