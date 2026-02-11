import { ReactNode } from 'react';

export interface FormFieldProps {
  label?: string;
  required?: boolean;
  helperText?: string;
  errorText?: string;
  children: ReactNode;
  htmlFor?: string;
}

export const FormField = ({
  label,
  required = false,
  helperText,
  errorText,
  children,
  htmlFor
}: FormFieldProps) => {
  const containerStyles: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xs)',
    fontFamily: 'var(--js-font-system)'
  };

  const labelStyles: React.CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-medium)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)'
  };

  const requiredStyles: React.CSSProperties = {
    color: 'var(--js-error)',
    marginLeft: '2px'
  };

  const helperStyles: React.CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.6
  };

  const errorStyles: React.CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-error)',
    display: 'flex',
    alignItems: 'flex-start',
    gap: 'var(--js-space-xs)'
  };

  return (
    <div style={containerStyles}>
      {label && (
        <label htmlFor={htmlFor} style={labelStyles}>
          {label}
          {required && <span style={requiredStyles}>*</span>}
        </label>
      )}
      {children}
      {!errorText && helperText && <span style={helperStyles}>{helperText}</span>}
      {errorText && <span style={errorStyles}>{errorText}</span>}
    </div>
  );
};
