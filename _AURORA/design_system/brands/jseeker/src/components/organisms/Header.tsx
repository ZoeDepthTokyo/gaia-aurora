import { CSSProperties, ReactNode } from 'react';
import { Menu, Bell, User, Settings } from 'lucide-react';
import { Button } from '../atoms/Button';
import { Badge } from '../molecules/Badge';

export interface NavigationItem {
  label: string;
  href?: string;
  onClick?: () => void;
  active?: boolean;
  badge?: number;
}

export interface HeaderProps {
  logo?: ReactNode;
  title?: string;
  navigation?: NavigationItem[];
  notifications?: number;
  userMenu?: {
    name: string;
    email?: string;
    avatar?: string;
  };
  onMenuClick?: () => void;
  onNotificationClick?: () => void;
  onUserClick?: () => void;
}

export const Header = ({
  logo,
  title = 'jSeeker',
  navigation = [],
  notifications = 0,
  userMenu,
  onMenuClick,
  onNotificationClick,
  onUserClick
}: HeaderProps) => {
  const headerStyles: CSSProperties = {
    position: 'sticky',
    top: 0,
    zIndex: 50,
    backgroundColor: 'var(--js-surface)',
    borderBottom: `var(--js-border-width-thin) solid var(--js-border)`,
    boxShadow: 'var(--js-shadow-1)',
    fontFamily: 'var(--js-font-system)'
  };

  const containerStyles: CSSProperties = {
    height: 'var(--js-header-height)',
    maxWidth: 'var(--js-max-content-width)',
    margin: '0 auto',
    padding: '0 var(--js-space-lg)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 'var(--js-space-lg)'
  };

  const leftSectionStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-lg)',
    flex: 1
  };

  const logoStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-sm)',
    textDecoration: 'none',
    color: 'var(--js-text)'
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-bold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: 0
  };

  const navStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-md)'
  };

  const navItemStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-medium)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    textDecoration: 'none',
    padding: '8px 12px',
    borderRadius: 'var(--js-border-radius-sm)',
    cursor: 'pointer',
    transition: 'all 200ms',
    background: 'none',
    border: 'none',
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-xs)'
  };

  const activeNavItemStyles: CSSProperties = {
    ...navItemStyles,
    backgroundColor: 'var(--js-bg)',
    color: 'var(--js-primary)',
    fontWeight: 'var(--js-font-weight-semibold)'
  };

  const rightSectionStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-sm)'
  };

  const iconButtonStyles: CSSProperties = {
    position: 'relative',
    background: 'none',
    border: 'none',
    padding: 'var(--js-space-sm)',
    cursor: 'pointer',
    color: 'var(--js-text)',
    opacity: 0.7,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 'var(--js-border-radius-sm)',
    transition: 'all 200ms'
  };

  const notificationBadgeStyles: CSSProperties = {
    position: 'absolute',
    top: '4px',
    right: '4px',
    minWidth: '16px',
    height: '16px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '10px',
    fontWeight: 'var(--js-font-weight-semibold)',
    color: 'var(--js-bg)',
    backgroundColor: 'var(--js-error)',
    borderRadius: 'var(--js-border-radius-full)',
    padding: '0 4px'
  };

  const userAvatarStyles: CSSProperties = {
    width: '32px',
    height: '32px',
    borderRadius: 'var(--js-border-radius-full)',
    backgroundColor: 'var(--js-primary)',
    color: 'var(--js-bg)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'var(--js-font-size-caption)',
    fontWeight: 'var(--js-font-weight-semibold)',
    cursor: 'pointer',
    border: `2px solid var(--js-border)`
  };

  return (
    <header style={headerStyles}>
      <div style={containerStyles}>
        <div style={leftSectionStyles}>
          {onMenuClick && (
            <button
              onClick={onMenuClick}
              style={iconButtonStyles}
              className="mobile-only"
              onMouseEnter={(e) => {
                e.currentTarget.style.opacity = '1';
                e.currentTarget.style.backgroundColor = 'var(--js-bg)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.opacity = '0.7';
                e.currentTarget.style.backgroundColor = 'transparent';
              }}
            >
              <Menu size={24} />
            </button>
          )}

          <a href="/" style={logoStyles}>
            {logo}
            <h1 style={titleStyles}>{title}</h1>
          </a>

          {navigation.length > 0 && (
            <nav style={navStyles} className="desktop-only">
              {navigation.map((item, index) => (
                <button
                  key={index}
                  onClick={item.onClick}
                  style={item.active ? activeNavItemStyles : navItemStyles}
                  onMouseEnter={(e) => {
                    if (!item.active) {
                      e.currentTarget.style.backgroundColor = 'var(--js-bg)';
                      e.currentTarget.style.opacity = '1';
                    }
                  }}
                  onMouseLeave={(e) => {
                    if (!item.active) {
                      e.currentTarget.style.backgroundColor = 'transparent';
                      e.currentTarget.style.opacity = '0.7';
                    }
                  }}
                >
                  {item.label}
                  {item.badge && item.badge > 0 && (
                    <Badge variant="primary" style={{ marginLeft: 'var(--js-space-xs)' }}>
                      {item.badge}
                    </Badge>
                  )}
                </button>
              ))}
            </nav>
          )}
        </div>

        <div style={rightSectionStyles}>
          {onNotificationClick && (
            <button
              onClick={onNotificationClick}
              style={iconButtonStyles}
              onMouseEnter={(e) => {
                e.currentTarget.style.opacity = '1';
                e.currentTarget.style.backgroundColor = 'var(--js-bg)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.opacity = '0.7';
                e.currentTarget.style.backgroundColor = 'transparent';
              }}
            >
              <Bell size={20} />
              {notifications > 0 && (
                <span style={notificationBadgeStyles}>{notifications}</span>
              )}
            </button>
          )}

          {userMenu && (
            <button
              onClick={onUserClick}
              style={userAvatarStyles}
            >
              {userMenu.avatar ? (
                <img
                  src={userMenu.avatar}
                  alt={userMenu.name}
                  style={{
                    width: '100%',
                    height: '100%',
                    borderRadius: 'var(--js-border-radius-full)',
                    objectFit: 'cover'
                  }}
                />
              ) : (
                userMenu.name.charAt(0).toUpperCase()
              )}
            </button>
          )}
        </div>
      </div>
    </header>
  );
};
