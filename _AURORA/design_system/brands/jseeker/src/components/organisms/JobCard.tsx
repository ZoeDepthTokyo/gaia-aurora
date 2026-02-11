import { CSSProperties } from 'react';
import { Briefcase, MapPin, DollarSign, Clock, ExternalLink } from 'lucide-react';
import { Card } from '../molecules/Card';
import { Badge } from '../molecules/Badge';
import { Button } from '../atoms/Button';

export interface JobCardProps {
  company: string;
  logo?: string;
  title: string;
  location: string;
  salary?: string;
  type: 'full-time' | 'part-time' | 'contract' | 'remote';
  postedDate: string;
  description: string;
  tags?: string[];
  status?: 'active' | 'saved' | 'closed' | 'archived';
  onApply?: () => void;
  onSave?: () => void;
  onClick?: () => void;
}

export const JobCard = ({
  company,
  logo,
  title,
  location,
  salary,
  type,
  postedDate,
  description,
  tags = [],
  status = 'active',
  onApply,
  onSave,
  onClick
}: JobCardProps) => {
  const headerStyles: CSSProperties = {
    display: 'flex',
    gap: 'var(--js-space-md)',
    marginBottom: 'var(--js-space-md)'
  };

  const logoStyles: CSSProperties = {
    width: '48px',
    height: '48px',
    borderRadius: 'var(--js-border-radius-sm)',
    backgroundColor: 'var(--js-surface)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    color: 'var(--js-text)',
    flexShrink: 0,
    border: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: '0 0 4px 0'
  };

  const companyStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    opacity: 0.7,
    margin: 0
  };

  const metaStyles: CSSProperties = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 'var(--js-space-md)',
    marginBottom: 'var(--js-space-md)',
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.7
  };

  const metaItemStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-xs)'
  };

  const descriptionStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    opacity: 0.8,
    margin: '0 0 var(--js-space-md) 0',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    display: '-webkit-box',
    WebkitLineClamp: 3,
    WebkitBoxOrient: 'vertical'
  };

  const tagsStyles: CSSProperties = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 'var(--js-space-xs)',
    marginBottom: 'var(--js-space-md)'
  };

  const footerStyles: CSSProperties = {
    display: 'flex',
    gap: 'var(--js-space-sm)',
    paddingTop: 'var(--js-space-md)',
    borderTop: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const statusBadgeMap = {
    active: 'job-active',
    saved: 'job-saved',
    closed: 'job-closed',
    archived: 'job-archived'
  } as const;

  return (
    <Card padding="default" elevation={1} hoverable onClick={onClick}>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 'var(--js-space-md)' }}>
        <div style={headerStyles}>
          <div style={logoStyles}>
            {logo ? <img src={logo} alt={company} style={{ width: '100%', height: '100%', objectFit: 'cover' }} /> : company[0]}
          </div>
          <div>
            <h3 style={titleStyles}>{title}</h3>
            <p style={companyStyles}>{company}</p>
          </div>
        </div>
        <Badge variant={statusBadgeMap[status]}>{status}</Badge>
      </div>

      <div style={metaStyles}>
        <span style={metaItemStyles}>
          <MapPin size={14} />
          {location}
        </span>
        {salary && (
          <span style={metaItemStyles}>
            <DollarSign size={14} />
            {salary}
          </span>
        )}
        <span style={metaItemStyles}>
          <Briefcase size={14} />
          {type}
        </span>
        <span style={metaItemStyles}>
          <Clock size={14} />
          {postedDate}
        </span>
      </div>

      <p style={descriptionStyles}>{description}</p>

      {tags.length > 0 && (
        <div style={tagsStyles}>
          {tags.map((tag, index) => (
            <Badge key={index} variant="default">
              {tag}
            </Badge>
          ))}
        </div>
      )}

      <div style={footerStyles}>
        {onApply && status === 'active' && (
          <Button
            variant="primary"
            size="sm"
            onClick={(e) => {
              e.stopPropagation();
              onApply();
            }}
            iconRight={<ExternalLink size={16} />}
          >
            Apply
          </Button>
        )}
        {onSave && (
          <Button
            variant="ghost"
            size="sm"
            onClick={(e) => {
              e.stopPropagation();
              onSave();
            }}
          >
            {status === 'saved' ? 'Unsave' : 'Save'}
          </Button>
        )}
      </div>
    </Card>
  );
};
