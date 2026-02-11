import { InputHTMLAttributes, forwardRef } from 'react';

export interface RadioProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: string;
  error?: boolean;
}

export const Radio = forwardRef<HTMLInputElement, RadioProps>(
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

    const radioWrapperStyles: React.CSSProperties = {
      position: 'relative',
      width: '20px',
      height: '20px',
      flexShrink: 0
    };

    const radioStyles: React.CSSProperties = {
      position: 'absolute',
      opacity: 0,
      width: '100%',
      height: '100%',
      margin: 0,
      cursor: disabled ? 'not-allowed' : 'pointer'
    };

    const customRadioStyles: React.CSSProperties = {
      width: '20px',
      height: '20px',
      border: `var(--js-border-width-thin) solid ${error ? 'var(--js-error)' : 'var(--js-border)'}`,
      borderRadius: 'var(--js-border-radius-full)',
      backgroundColor: 'var(--js-bg)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      transition: 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)',
      pointerEvents: 'none'
    };

    const dotStyles: React.CSSProperties = {
      width: '10px',
      height: '10px',
      borderRadius: 'var(--js-border-radius-full)',
      backgroundColor: 'var(--js-bg)',
      opacity: props.checked ? 1 : 0,
      transition: 'opacity 200ms cubic-bezier(0.4, 0, 0.2, 1)'
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
        <div style={radioWrapperStyles}>
          <input
            ref={ref}
            type="radio"
            disabled={disabled}
            style={radioStyles}
            {...props}
            onChange={(e) => {
              const customRadio = e.currentTarget.nextElementSibling as HTMLElement;
              if (e.currentTarget.checked) {
                customRadio.style.backgroundColor = error ? 'var(--js-error)' : 'var(--js-primary)';
                customRadio.style.borderColor = error ? 'var(--js-error)' : 'var(--js-primary)';
              }
              props.onChange?.(e);
            }}
            onFocus={(e) => {
              const customRadio = e.currentTarget.nextElementSibling as HTMLElement;
              customRadio.style.boxShadow = `0 0 0 3px ${error ? 'rgba(220, 38, 38, 0.1)' : 'rgba(30, 58, 138, 0.1)'}`;
              props.onFocus?.(e);
            }}
            onBlur={(e) => {
              const customRadio = e.currentTarget.nextElementSibling as HTMLElement;
              customRadio.style.boxShadow = 'none';
              props.onBlur?.(e);
            }}
          />
          <div style={customRadioStyles}>
            <div style={dotStyles} />
          </div>
        </div>
        {label && <span style={labelStyles}>{label}</span>}
      </label>
    );
  }
);

Radio.displayName = 'Radio';
