import { TextareaHTMLAttributes, forwardRef } from 'react';

export interface TextareaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  error?: boolean;
  success?: boolean;
  fullWidth?: boolean;
  resize?: 'none' | 'vertical' | 'horizontal' | 'both';
}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  (
    {
      error = false,
      success = false,
      fullWidth = false,
      resize = 'vertical',
      disabled,
      className = '',
      style = {},
      ...props
    },
    ref
  ) => {
    const baseTextareaStyles: React.CSSProperties = {
      fontFamily: 'var(--js-font-system)',
      fontSize: 'var(--js-font-size-body)',
      fontWeight: 'var(--js-font-weight-regular)',
      lineHeight: 'var(--js-line-height-body)',
      color: 'var(--js-text)',
      backgroundColor: 'var(--js-bg)',
      border: `var(--js-border-width-thin) solid var(--js-border)`,
      borderRadius: 'var(--js-border-radius-md)',
      padding: 'var(--js-space-sm) var(--js-space-md)',
      minHeight: '80px',
      width: fullWidth ? '100%' : 'auto',
      outline: 'none',
      resize: resize,
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      ...style
    };

    if (error) {
      baseTextareaStyles.borderColor = 'var(--js-error)';
    } else if (success) {
      baseTextareaStyles.borderColor = 'var(--js-success)';
    }

    if (disabled) {
      baseTextareaStyles.opacity = 0.5;
      baseTextareaStyles.cursor = 'not-allowed';
      baseTextareaStyles.backgroundColor = 'var(--js-surface)';
    }

    return (
      <textarea
        ref={ref}
        disabled={disabled}
        style={baseTextareaStyles}
        className={className}
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
    );
  }
);

Textarea.displayName = 'Textarea';
