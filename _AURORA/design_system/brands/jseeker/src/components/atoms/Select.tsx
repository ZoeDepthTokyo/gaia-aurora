import { SelectHTMLAttributes, forwardRef, ReactNode } from 'react';
import { ChevronDown } from 'lucide-react';

export interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement> {
  error?: boolean;
  success?: boolean;
  prefixIcon?: ReactNode;
  fullWidth?: boolean;
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
  (
    {
      error = false,
      success = false,
      prefixIcon,
      fullWidth = false,
      disabled,
      className = '',
      style = {},
      children,
      ...props
    },
    ref
  ) => {
    const containerStyles: React.CSSProperties = {
      display: 'inline-flex',
      alignItems: 'center',
      position: 'relative',
      width: fullWidth ? '100%' : 'auto',
      fontFamily: 'var(--js-font-system)'
    };

    const baseSelectStyles: React.CSSProperties = {
      fontFamily: 'var(--js-font-system)',
      fontSize: 'var(--js-font-size-body)',
      fontWeight: 'var(--js-font-weight-regular)',
      lineHeight: 'var(--js-line-height-body)',
      color: 'var(--js-text)',
      backgroundColor: 'var(--js-bg)',
      border: `var(--js-border-width-thin) solid var(--js-border)`,
      borderRadius: 'var(--js-border-radius-md)',
      padding: 'var(--js-space-sm) var(--js-space-md)',
      paddingRight: '40px',
      minHeight: '40px',
      width: '100%',
      outline: 'none',
      appearance: 'none',
      cursor: disabled ? 'not-allowed' : 'pointer',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      ...style
    };

    if (prefixIcon) {
      baseSelectStyles.paddingLeft = '40px';
    }

    if (error) {
      baseSelectStyles.borderColor = 'var(--js-error)';
    } else if (success) {
      baseSelectStyles.borderColor = 'var(--js-success)';
    }

    if (disabled) {
      baseSelectStyles.opacity = 0.5;
      baseSelectStyles.backgroundColor = 'var(--js-surface)';
    }

    const prefixIconStyles: React.CSSProperties = {
      position: 'absolute',
      left: '12px',
      top: '50%',
      transform: 'translateY(-50%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      pointerEvents: 'none',
      color: 'var(--js-text)',
      opacity: 0.5
    };

    const chevronStyles: React.CSSProperties = {
      position: 'absolute',
      right: '12px',
      top: '50%',
      transform: 'translateY(-50%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      pointerEvents: 'none',
      color: 'var(--js-text)',
      opacity: 0.5
    };

    return (
      <div style={containerStyles} className={className}>
        {prefixIcon && <span style={prefixIconStyles}>{prefixIcon}</span>}
        <select
          ref={ref}
          disabled={disabled}
          style={baseSelectStyles}
          {...props}
          onFocus={(e) => {
            if (!disabled) {
              const target = e.currentTarget;
              if (error) {
                target.style.borderColor = 'var(--js-error)';
                target.style.boxShadow = '0 0 0 3px rgba(220, 38, 38, 0.1)';
              } else if (success) {
                target.style.borderColor = 'var(--js-success)';
                target.style.boxShadow = '0 0 0 3px rgba(16, 185, 129, 0.1)';
              } else {
                target.style.borderColor = 'var(--js-primary)';
                target.style.boxShadow = '0 0 0 3px rgba(30, 58, 138, 0.1)';
              }
            }
            props.onFocus?.(e);
          }}
          onBlur={(e) => {
            const target = e.currentTarget;
            target.style.boxShadow = 'none';
            if (error) {
              target.style.borderColor = 'var(--js-error)';
            } else if (success) {
              target.style.borderColor = 'var(--js-success)';
            } else {
              target.style.borderColor = 'var(--js-border)';
            }
            props.onBlur?.(e);
          }}
        >
          {children}
        </select>
        <span style={chevronStyles}>
          <ChevronDown size={20} />
        </span>
      </div>
    );
  }
);

Select.displayName = 'Select';
