import { InputHTMLAttributes, forwardRef, ReactNode } from 'react';

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  error?: boolean;
  success?: boolean;
  prefixIcon?: ReactNode;
  suffixIcon?: ReactNode;
  fullWidth?: boolean;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      error = false,
      success = false,
      prefixIcon,
      suffixIcon,
      fullWidth = false,
      disabled,
      className = '',
      style = {},
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

    const baseInputStyles: React.CSSProperties = {
      fontFamily: 'var(--js-font-system)',
      fontSize: 'var(--js-font-size-body)',
      fontWeight: 'var(--js-font-weight-regular)',
      lineHeight: 'var(--js-line-height-body)',
      color: 'var(--js-text)',
      backgroundColor: 'var(--js-bg)',
      border: `var(--js-border-width-thin) solid var(--js-border)`,
      borderRadius: 'var(--js-border-radius-md)',
      padding: 'var(--js-space-sm) var(--js-space-md)',
      minHeight: '40px',
      width: '100%',
      outline: 'none',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      ...style
    };

    // Add padding for icons
    if (prefixIcon) {
      baseInputStyles.paddingLeft = '40px';
    }
    if (suffixIcon) {
      baseInputStyles.paddingRight = '40px';
    }

    // State styles
    if (error) {
      baseInputStyles.borderColor = 'var(--js-error)';
    } else if (success) {
      baseInputStyles.borderColor = 'var(--js-success)';
    }

    if (disabled) {
      baseInputStyles.opacity = 0.5;
      baseInputStyles.cursor = 'not-allowed';
      baseInputStyles.backgroundColor = 'var(--js-surface)';
    }

    const iconStyles: React.CSSProperties = {
      position: 'absolute',
      top: '50%',
      transform: 'translateY(-50%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      pointerEvents: 'none',
      color: 'var(--js-text)',
      opacity: 0.5
    };

    const prefixIconStyles: React.CSSProperties = {
      ...iconStyles,
      left: '12px'
    };

    const suffixIconStyles: React.CSSProperties = {
      ...iconStyles,
      right: '12px'
    };

    return (
      <div style={containerStyles} className={className}>
        {prefixIcon && <span style={prefixIconStyles}>{prefixIcon}</span>}
        <input
          ref={ref}
          disabled={disabled}
          style={baseInputStyles}
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
        />
        {suffixIcon && <span style={suffixIconStyles}>{suffixIcon}</span>}
      </div>
    );
  }
);

Input.displayName = 'Input';
