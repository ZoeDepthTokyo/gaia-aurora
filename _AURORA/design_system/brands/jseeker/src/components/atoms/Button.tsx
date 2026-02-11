import { ButtonHTMLAttributes, forwardRef, ReactNode } from 'react';
import { Loader2 } from 'lucide-react';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost' | 'destructive';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  iconLeft?: ReactNode;
  iconRight?: ReactNode;
  fullWidth?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = 'primary',
      size = 'md',
      isLoading = false,
      iconLeft,
      iconRight,
      fullWidth = false,
      disabled,
      children,
      className = '',
      style = {},
      ...props
    },
    ref
  ) => {
    const baseStyles: React.CSSProperties = {
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'var(--js-font-system)',
      fontWeight: 'var(--js-font-weight-medium)',
      lineHeight: 'var(--js-line-height-body)',
      borderRadius: 'var(--js-border-radius-md)',
      cursor: disabled || isLoading ? 'not-allowed' : 'pointer',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      border: 'none',
      outline: 'none',
      width: fullWidth ? '100%' : 'auto',
      opacity: disabled ? 0.5 : 1,
      ...style
    };

    // Size styles
    const sizeStyles: Record<string, React.CSSProperties> = {
      sm: {
        fontSize: 'var(--js-font-size-caption)',
        padding: '6px 12px',
        gap: 'var(--js-space-xs)',
        minHeight: '32px'
      },
      md: {
        fontSize: 'var(--js-font-size-body)',
        padding: 'var(--js-space-sm) var(--js-space-md)',
        gap: 'var(--js-space-sm)',
        minHeight: '40px'
      },
      lg: {
        fontSize: 'var(--js-font-size-body-l)',
        padding: '12px 24px',
        gap: 'var(--js-space-sm)',
        minHeight: 'var(--js-min-touch-target)'
      }
    };

    // Variant styles
    const variantStyles: Record<string, React.CSSProperties> = {
      primary: {
        backgroundColor: 'var(--js-primary)',
        color: 'var(--js-bg)',
        border: 'var(--js-border-width-thin) solid var(--js-primary)'
      },
      secondary: {
        backgroundColor: 'var(--js-bg)',
        color: 'var(--js-text)',
        border: 'var(--js-border-width-thin) solid var(--js-border)'
      },
      ghost: {
        backgroundColor: 'transparent',
        color: 'var(--js-text)',
        border: 'var(--js-border-width-thin) solid transparent'
      },
      destructive: {
        backgroundColor: 'var(--js-error)',
        color: 'var(--js-bg)',
        border: 'var(--js-border-width-thin) solid var(--js-error)'
      }
    };

    const combinedStyles = {
      ...baseStyles,
      ...sizeStyles[size],
      ...variantStyles[variant]
    };

    const iconSize = size === 'sm' ? 16 : size === 'md' ? 20 : 24;

    return (
      <button
        ref={ref}
        disabled={disabled || isLoading}
        className={className}
        style={combinedStyles}
        {...props}
        onMouseEnter={(e) => {
          if (!disabled && !isLoading) {
            const target = e.currentTarget as HTMLButtonElement;
            if (variant === 'primary') {
              target.style.backgroundColor = 'var(--js-primary-hover)';
              target.style.borderColor = 'var(--js-primary-hover)';
            } else if (variant === 'secondary') {
              target.style.backgroundColor = 'var(--js-surface)';
            } else if (variant === 'ghost') {
              target.style.backgroundColor = 'var(--js-surface)';
            } else if (variant === 'destructive') {
              target.style.opacity = '0.9';
            }
          }
          props.onMouseEnter?.(e);
        }}
        onMouseLeave={(e) => {
          if (!disabled && !isLoading) {
            const target = e.currentTarget as HTMLButtonElement;
            if (variant === 'primary') {
              target.style.backgroundColor = 'var(--js-primary)';
              target.style.borderColor = 'var(--js-primary)';
            } else if (variant === 'secondary') {
              target.style.backgroundColor = 'var(--js-bg)';
            } else if (variant === 'ghost') {
              target.style.backgroundColor = 'transparent';
            } else if (variant === 'destructive') {
              target.style.opacity = '1';
            }
          }
          props.onMouseLeave?.(e);
        }}
        onMouseDown={(e) => {
          if (!disabled && !isLoading) {
            const target = e.currentTarget as HTMLButtonElement;
            if (variant === 'primary') {
              target.style.backgroundColor = 'var(--js-primary-active)';
              target.style.borderColor = 'var(--js-primary-active)';
            }
            target.style.transform = 'translateY(1px)';
          }
          props.onMouseDown?.(e);
        }}
        onMouseUp={(e) => {
          if (!disabled && !isLoading) {
            const target = e.currentTarget as HTMLButtonElement;
            target.style.transform = 'translateY(0)';
          }
          props.onMouseUp?.(e);
        }}
      >
        {isLoading && (
          <Loader2
            size={iconSize}
            style={{ animation: 'spin 1s linear infinite' }}
          />
        )}
        {!isLoading && iconLeft && <span style={{ display: 'flex', alignItems: 'center' }}>{iconLeft}</span>}
        {children && <span>{children}</span>}
        {!isLoading && iconRight && <span style={{ display: 'flex', alignItems: 'center' }}>{iconRight}</span>}
      </button>
    );
  }
);

Button.displayName = 'Button';
