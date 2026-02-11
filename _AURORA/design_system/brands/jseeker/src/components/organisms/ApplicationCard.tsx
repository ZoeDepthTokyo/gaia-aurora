import { CSSProperties } from 'react';
import { Calendar, DollarSign, TrendingUp, MoreVertical } from 'lucide-react';
import { Card } from '../molecules/Card';
import { Badge } from '../molecules/Badge';

export type ApplicationStatus = 'applied' | 'interviewing' | 'offered' | 'rejected' | 'withdrawn';

export interface ApplicationCardProps {
  company: string;
  logo?: string;
  position: string;
  status: ApplicationStatus;
  appliedDate: string;
  salary?: string;
  atsScore?: number;
  nextStep?: {
    type: string;
    date: string;
  };
  notes?: string;
  onClick?: () => void;
}

export const ApplicationCard = ({
  company,
  logo,
  position,
  status,
  appliedDate,
  salary,
  atsScore,
  nextStep,
  notes,
  onClick
}: ApplicationCardProps) => {
  const headerStyles: CSSProperties = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 'var(--js-space-md)'
  };

  const companyInfoStyles: CSSProperties = {
    display: 'flex',
    gap: 'var(--js-space-md)',
    flex: 1
  };

  const logoStyles: CSSProperties = {
    width: '40px',
    height: '40px',
    borderRadius: 'var(--js-border-radius-sm)',
    backgroundColor: 'var(--js-surface)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-semibold)',
    color: 'var(--js-text)',
    flexShrink: 0,
    border: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const positionStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    margin: '0 0 2px 0'
  };

  const companyStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.6,
    margin: 0
  };

  const statusBadgeMap: Record<ApplicationStatus, any> = {
    applied: 'app-applied',
    interviewing: 'app-interviewing',
    offered: 'app-offered',
    rejected: 'app-rejected',
    withdrawn: 'app-withdrawn'
  };

  const metricsStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))',
    gap: 'var(--js-space-md)',
    padding: 'var(--js-space-md)',
    backgroundColor: 'var(--js-bg)',
    borderRadius: 'var(--js-border-radius-sm)',
    marginBottom: 'var(--js-space-md)'
  };

  const metricStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px'
  };

  const metricLabelStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.5,
    textTransform: 'uppercase',
    letterSpacing: 'var(--js-letter-spacing-uppercase)',
    fontWeight: 'var(--js-font-weight-semibold)'
  };

  const metricValueStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-xs)'
  };

  const atsScoreStyles: CSSProperties = {
    ...metricValueStyles,
    fontFamily: 'var(--js-font-mono)',
    fontSize: 'var(--js-font-size-h3)',
    color: atsScore && atsScore >= 80 ? 'var(--js-success)' : atsScore && atsScore >= 60 ? 'var(--js-warning)' : 'var(--js-error)'
  };

  const notesStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.7,
    padding: 'var(--js-space-sm)',
    backgroundColor: 'var(--js-bg)',
    borderRadius: 'var(--js-border-radius-sm)',
    borderLeft: `2px solid var(--js-primary)`
  };

  return (
    <Card padding="default" elevation={1} hoverable onClick={onClick}>
      <div style={headerStyles}>
        <div style={companyInfoStyles}>
          <div style={logoStyles}>
            {logo ? <img src={logo} alt={company} style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: 'var(--js-border-radius-sm)' }} /> : company[0]}
          </div>
          <div>
            <h3 style={positionStyles}>{position}</h3>
            <p style={companyStyles}>{company}</p>
          </div>
        </div>
        <Badge variant={statusBadgeMap[status]}>{status}</Badge>
      </div>

      <div style={metricsStyles}>
        <div style={metricStyles}>
          <span style={metricLabelStyles}>Applied</span>
          <span style={metricValueStyles}>
            <Calendar size={14} />
            {appliedDate}
          </span>
        </div>

        {salary && (
          <div style={metricStyles}>
            <span style={metricLabelStyles}>Salary</span>
            <span style={metricValueStyles}>
              <DollarSign size={14} />
              {salary}
            </span>
          </div>
        )}

        {atsScore !== undefined && (
          <div style={metricStyles}>
            <span style={metricLabelStyles}>ATS Score</span>
            <span style={atsScoreStyles}>
              <TrendingUp size={14} />
              {atsScore}%
            </span>
          </div>
        )}

        {nextStep && (
          <div style={metricStyles}>
            <span style={metricLabelStyles}>Next Step</span>
            <span style={metricValueStyles}>
              {nextStep.type}
            </span>
            <span style={{ fontSize: 'var(--js-font-size-caption)', opacity: 0.6 }}>
              {nextStep.date}
            </span>
          </div>
        )}
      </div>

      {notes && (
        <div style={notesStyles}>
          {notes}
        </div>
      )}
    </Card>
  );
};
