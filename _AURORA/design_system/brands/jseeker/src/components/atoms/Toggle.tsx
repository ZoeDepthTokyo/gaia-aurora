import { InputHTMLAttributes, forwardRef } from 'react';

export interface ToggleProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: string;
  error?: boolean;
}

export const Toggle = forwardRef<HTMLInputElement, ToggleProps>(
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

    const toggleWrapperStyles: React.CSSProperties = {
      position: 'relative',
      width: '44px',
      height: '24px',
      flexShrink: 0
    };

    const toggleInputStyles: React.CSSProperties = {
      position: 'absolute',
      opacity: 0,
      width: '100%',
      height: '100%',
      margin: 0,
      cursor: disabled ? 'not-allowed' : 'pointer'
    };

    const toggleTrackStyles: React.CSSProperties = {
      width: '44px',
      height: '24px',
      border: `var(--js-border-width-thin) solid ${error ? 'var(--js-error)' : 'var(--js-border)'}`,
      borderRadius: 'var(--js-border-radius-full)',
      backgroundColor: 'var(--js-surface)',
      display: 'flex',
      alignItems: 'center',
      padding: '2px',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      pointerEvents: 'none'
    };

    const toggleThumbStyles: React.CSSProperties = {
      width: '18px',
      height: '18px',
      borderRadius: 'var(--js-border-radius-full)',
      backgroundColor: 'var(--js-bg)',
      boxShadow: 'var(--js-shadow-1)',
      transition: 'transform 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      transform: props.checked ? 'translateX(20px)' : 'translateX(0)'
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
        <div style={toggleWrapperStyles}>
          <input
            ref={ref}
            type="checkbox"
            disabled={disabled}
            style={toggleInputStyles}
            {...props}
            onChange={(e) => {
              const track = e.currentTarget.nextElementSibling as HTMLElement;
              const thumb = track.firstChild as HTMLElement;

              if (e.currentTarget.checked) {
                track.style.backgroundColor = error ? 'var(--js-error)' : 'var(--js-primary)';
                track.style.borderColor = error ? 'var(--js-error)' : 'var(--js-primary)';
                thumb.style.transform = 'translateX(20px)';
              } else {
                track.style.backgroundColor = 'var(--js-surface)';
                track.style.borderColor = error ? 'var(--js-error)' : 'var(--js-border)';
                thumb.style.transform = 'translateX(0)';
              }
              props.onChange?.(e);
            }}
            onFocus={(e) => {
              const track = e.currentTarget.nextElementSibling as HTMLElement;
              track.style.boxShadow = `0 0 0 3px ${error ? 'rgba(220, 38, 38, 0.1)' : 'rgba(30, 58, 138, 0.1)'}`;
              props.onFocus?.(e);
            }}
            onBlur={(e) => {
              const track = e.currentTarget.nextElementSibling as HTMLElement;
              track.style.boxShadow = 'none';
              props.onBlur?.(e);
            }}
          />
          <div style={toggleTrackStyles}>
            <div style={toggleThumbStyles} />
          </div>
        </div>
        {label && <span style={labelStyles}>{label}</span>}
      </label>
    );
  }
);

Toggle.displayName = 'Toggle';
