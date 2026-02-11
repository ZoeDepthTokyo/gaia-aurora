import { CSSProperties, useState } from 'react';
import { Plus, Trash2, FileText } from 'lucide-react';
import { Card, CardHeader } from '../molecules/Card';
import { FormField } from '../molecules/FormField';
import { Input } from '../atoms/Input';
import { Textarea } from '../atoms/Textarea';
import { Button } from '../atoms/Button';
import { Badge } from '../molecules/Badge';

export interface ResumeData {
  personalInfo: {
    name: string;
    email: string;
    phone: string;
    location: string;
    linkedin?: string;
  };
  summary: string;
  experience: Array<{
    title: string;
    company: string;
    location: string;
    startDate: string;
    endDate: string;
    current: boolean;
    description: string;
  }>;
  education: Array<{
    degree: string;
    school: string;
    location: string;
    graduationDate: string;
  }>;
  skills: string[];
}

export interface ResumeBuilderFormProps {
  initialData?: Partial<ResumeData>;
  onSave?: (data: ResumeData) => void;
  onPreview?: () => void;
  atsScore?: number;
}

export const ResumeBuilderForm = ({
  initialData,
  onSave,
  onPreview,
  atsScore
}: ResumeBuilderFormProps) => {
  const [formData, setFormData] = useState<ResumeData>({
    personalInfo: {
      name: '',
      email: '',
      phone: '',
      location: '',
      linkedin: ''
    },
    summary: '',
    experience: [],
    education: [],
    skills: [],
    ...initialData
  });

  const [newSkill, setNewSkill] = useState('');

  const containerStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-lg)',
    fontFamily: 'var(--js-font-system)'
  };

  const sectionTitleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: 0
  };

  const gridStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: 'var(--js-space-md)'
  };

  const skillsContainerStyles: CSSProperties = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 'var(--js-space-xs)',
    marginTop: 'var(--js-space-sm)'
  };

  return (
    <div style={containerStyles}>
      {/* Header with ATS Score */}
      <Card padding="default" elevation={2}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--js-space-md)' }}>
            <FileText size={24} style={{ color: 'var(--js-primary)' }} />
            <h2 style={sectionTitleStyles}>Resume Builder</h2>
          </div>
          {atsScore !== undefined && (
            <div style={{ textAlign: 'right' }}>
              <div style={{
                fontSize: 'var(--js-font-size-metric)',
                fontWeight: 'var(--js-font-weight-semibold)',
                lineHeight: 'var(--js-line-height-metric)',
                fontFamily: 'var(--js-font-mono)',
                color: atsScore >= 80 ? 'var(--js-success)' : atsScore >= 60 ? 'var(--js-warning)' : 'var(--js-error)'
              }}>
                {atsScore}%
              </div>
              <div style={{
                fontSize: 'var(--js-font-size-caption)',
                color: 'var(--js-text)',
                opacity: 0.6
              }}>
                ATS Score
              </div>
            </div>
          )}
        </div>
      </Card>

      {/* Personal Information */}
      <Card padding="spacious" elevation={1}>
        <CardHeader title="Personal Information" />
        <div style={gridStyles}>
          <FormField label="Full Name" required>
            <Input
              placeholder="John Doe"
              value={formData.personalInfo.name}
              onChange={(e) => setFormData({
                ...formData,
                personalInfo: { ...formData.personalInfo, name: e.target.value }
              })}
              fullWidth
            />
          </FormField>
          <FormField label="Email" required>
            <Input
              type="email"
              placeholder="john@example.com"
              value={formData.personalInfo.email}
              onChange={(e) => setFormData({
                ...formData,
                personalInfo: { ...formData.personalInfo, email: e.target.value }
              })}
              fullWidth
            />
          </FormField>
          <FormField label="Phone">
            <Input
              type="tel"
              placeholder="(555) 123-4567"
              value={formData.personalInfo.phone}
              onChange={(e) => setFormData({
                ...formData,
                personalInfo: { ...formData.personalInfo, phone: e.target.value }
              })}
              fullWidth
            />
          </FormField>
          <FormField label="Location">
            <Input
              placeholder="San Francisco, CA"
              value={formData.personalInfo.location}
              onChange={(e) => setFormData({
                ...formData,
                personalInfo: { ...formData.personalInfo, location: e.target.value }
              })}
              fullWidth
            />
          </FormField>
        </div>
      </Card>

      {/* Professional Summary */}
      <Card padding="spacious" elevation={1}>
        <CardHeader title="Professional Summary" />
        <FormField
          helperText="2-3 sentences highlighting your key qualifications and career objectives"
        >
          <Textarea
            placeholder="Experienced product manager with 5+ years building SaaS products..."
            value={formData.summary}
            onChange={(e) => setFormData({ ...formData, summary: e.target.value })}
            fullWidth
            rows={4}
          />
        </FormField>
      </Card>

      {/* Skills */}
      <Card padding="spacious" elevation={1}>
        <CardHeader
          title="Skills"
          action={
            <div style={{ display: 'flex', gap: 'var(--js-space-sm)' }}>
              <Input
                placeholder="Add skill..."
                value={newSkill}
                onChange={(e) => setNewSkill(e.target.value)}
                onKeyPress={(e) => {
                  if (e.key === 'Enter' && newSkill.trim()) {
                    setFormData({
                      ...formData,
                      skills: [...formData.skills, newSkill.trim()]
                    });
                    setNewSkill('');
                  }
                }}
              />
              <Button
                size="sm"
                iconLeft={<Plus size={16} />}
                onClick={() => {
                  if (newSkill.trim()) {
                    setFormData({
                      ...formData,
                      skills: [...formData.skills, newSkill.trim()]
                    });
                    setNewSkill('');
                  }
                }}
              >
                Add
              </Button>
            </div>
          }
        />
        <div style={skillsContainerStyles}>
          {formData.skills.map((skill, index) => (
            <Badge key={index} variant="default">
              {skill}
              <button
                onClick={() => {
                  setFormData({
                    ...formData,
                    skills: formData.skills.filter((_, i) => i !== index)
                  });
                }}
                style={{
                  background: 'none',
                  border: 'none',
                  padding: 0,
                  marginLeft: 'var(--js-space-xs)',
                  cursor: 'pointer',
                  display: 'inline-flex',
                  color: 'inherit'
                }}
              >
                <Trash2 size={12} />
              </button>
            </Badge>
          ))}
          {formData.skills.length === 0 && (
            <p style={{
              fontSize: 'var(--js-font-size-caption)',
              color: 'var(--js-text)',
              opacity: 0.6,
              margin: 0
            }}>
              No skills added yet. Add your key skills above.
            </p>
          )}
        </div>
      </Card>

      {/* Actions */}
      <div style={{
        display: 'flex',
        gap: 'var(--js-space-sm)',
        justifyContent: 'flex-end',
        paddingTop: 'var(--js-space-md)'
      }}>
        {onPreview && (
          <Button variant="secondary" onClick={onPreview}>
            Preview
          </Button>
        )}
        {onSave && (
          <Button
            variant="primary"
            onClick={() => onSave(formData)}
          >
            Save Resume
          </Button>
        )}
      </div>
    </div>
  );
};
