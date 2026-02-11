import { ReactNode, CSSProperties, FormEvent } from 'react';
import { Card } from '../molecules/Card';
import { Button } from '../atoms/Button';
import { Alert } from '../molecules/Alert';

export interface FormSection {
  title: string;
  description?: string;
  fields: ReactNode;
}

export interface FormTemplateProps {
  title: string;
  description?: string;
  sections: FormSection[];
  onSubmit: (e: FormEvent) => void;
  submitLabel?: string;
  cancelLabel?: string;
  onCancel?: () => void;
  isSubmitting?: boolean;
  error?: string;
  success?: string;
  fullWidth?: boolean;
}

export const FormTemplate = ({
  title,
  description,
  sections,
  onSubmit,
  submitLabel = 'Submit',
  cancelLabel = 'Cancel',
  onCancel,
  isSubmitting = false,
  error,
  success,
  fullWidth = false
}: FormTemplateProps) => {
  const containerStyles: CSSProperties = {
    maxWidth: fullWidth ? '100%' : '800px',
    margin: '0 auto',
    fontFamily: 'var(--js-font-system)'
  };

  const headerStyles: CSSProperties = {
    marginBottom: 'var(--js-space-xl)',
    paddingBottom: 'var(--js-space-lg)',
    borderBottom: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h1)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h1)',
    letterSpacing: 'var(--js-letter-spacing-display)',
    color: 'var(--js-text)',
    margin: '0 0 8px 0'
  };

  const descriptionStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body-l)',
    lineHeight: 'var(--js-line-height-body-l)',
    color: 'var(--js-text)',
    opacity: 0.7,
    margin: 0
  };

  const formStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xl)'
  };

  const sectionTitleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: '0 0 8px 0'
  };

  const sectionDescriptionStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.6,
    marginBottom: 'var(--js-space-md)'
  };

  const actionsStyles: CSSProperties = {
    display: 'flex',
    gap: 'var(--js-space-sm)',
    justifyContent: 'flex-end',
    paddingTop: 'var(--js-space-lg)',
    borderTop: `var(--js-border-width-thin) solid var(--js-border)`,
    marginTop: 'var(--js-space-lg)'
  };

  return (
    <div style={containerStyles}>
      {/* Header */}
      <div style={headerStyles}>
        <h1 style={titleStyles}>{title}</h1>
        {description && <p style={descriptionStyles}>{description}</p>}
      </div>

      {/* Error/Success Messages */}
      {error && (
        <div style={{ marginBottom: 'var(--js-space-lg)' }}>
          <Alert variant="error" title="Error">
            {error}
          </Alert>
        </div>
      )}
      {success && (
        <div style={{ marginBottom: 'var(--js-space-lg)' }}>
          <Alert variant="success" title="Success">
            {success}
          </Alert>
        </div>
      )}

      {/* Form */}
      <form onSubmit={onSubmit} style={formStyles}>
        {sections.map((section, index) => (
          <Card key={index} padding="spacious" elevation={1}>
            <h2 style={sectionTitleStyles}>{section.title}</h2>
            {section.description && (
              <p style={sectionDescriptionStyles}>{section.description}</p>
            )}
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: 'var(--js-space-md)'
            }}>
              {section.fields}
            </div>
          </Card>
        ))}

        {/* Actions */}
        <div style={actionsStyles}>
          {onCancel && (
            <Button
              type="button"
              variant="ghost"
              onClick={onCancel}
              disabled={isSubmitting}
            >
              {cancelLabel}
            </Button>
          )}
          <Button
            type="submit"
            variant="primary"
            disabled={isSubmitting}
          >
            {isSubmitting ? 'Submitting...' : submitLabel}
          </Button>
        </div>
      </form>
    </div>
  );
};
