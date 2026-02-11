import { InputHTMLAttributes, forwardRef } from 'react';
import { Check } from 'lucide-react';

export interface CheckboxProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: string;
  error?: boolean;
}

export const Checkbox = forwardRef<HTMLInputElement, CheckboxProps>(
  ({ label, error = false, disabled, className = '', style = {}, ...props }, ref) => {
    const containerStyles: React.CSSProperties = {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 'var(--js-space-sm)',
      cursor: disabled ? 'not-allowed' : 'pointer',
      fontFamily: 'var(--js-font-system)',
      opacity: disabled ? 0.5 : 1,
      ...style
    };

    const checkboxWrapperStyles: React.CSSProperties = {
      position: 'relative',
      width: '20px',
      height: '20px',
      flexShrink: 0
    };

    const checkboxStyles: React.CSSProperties = {
      position: 'absolute',
      opacity: 0,
      width: '100%',
      height: '100%',
      margin: 0,
      cursor: disabled ? 'not-allowed' : 'pointer'
    };

    const customCheckboxStyles: React.CSSProperties = {
      width: '20px',
      height: '20px',
      border: `var(--js-border-width-thin) solid ${error ? 'var(--js-error)' : 'var(--js-border)'}`,
      borderRadius: 'var(--js-border-radius-sm)',
      backgroundColor: 'var(--js-bg)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      pointerEvents: 'none'
    };

    const labelStyles: React.CSSProperties = {
      fontSize: 'var(--js-font-size-body)',
      lineHeight: 'var(--js-line-height-body)',
      fontWeight: 'var(--js-font-weight-regular)',
      color: error ? 'var(--js-error)' : 'var(--js-text)',
      userSelect: 'none'
    };

    return (
      <label style={containerStyles} className={className}>
        <div style={checkboxWrapperStyles}>
          <input
            ref={ref}
            type="checkbox"
            disabled={disabled}
            style={checkboxStyles}
            {...props}
            onChange={(e) => {
              const customBox = e.currentTarget.nextElementSibling as HTMLElement;
              if (e.currentTarget.checked) {
                customBox.style.backgroundColor = error ? 'var(--js-error)' : 'var(--js-primary)';
                customBox.style.borderColor = error ? 'var(--js-error)' : 'var(--js-primary)';
              } else {
                customBox.style.backgroundColor = 'var(--js-bg)';
                customBox.style.borderColor = error ? 'var(--js-error)' : 'var(--js-border)';
              }
              props.onChange?.(e);
            }}
            onFocus={(e) => {
              const customBox = e.currentTarget.nextElementSibling as HTMLElement;
              customBox.style.boxShadow = `0 0 0 3px ${error ? 'rgba(220, 38, 38, 0.1)' : 'rgba(30, 58, 138, 0.1)'}`;
              props.onFocus?.(e);
            }}
            onBlur={(e) => {
              const customBox = e.currentTarget.nextElementSibling as HTMLElement;
              customBox.style.boxShadow = 'none';
              props.onBlur?.(e);
            }}
          />
          <div style={customCheckboxStyles}>
            {props.checked && <Check size={14} style={{ color: 'var(--js-bg)' }} />}
          </div>
        </div>
        {label && <span style={labelStyles}>{label}</span>}
      </label>
    );
  }
);

Checkbox.displayName = 'Checkbox';
