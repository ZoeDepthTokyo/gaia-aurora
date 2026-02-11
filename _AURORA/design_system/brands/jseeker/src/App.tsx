import { useState } from 'react';
import { Moon, Sun, Plus, Briefcase, FileText, TrendingUp, DollarSign, Calendar, Target, Search, MapPin, Palette } from 'lucide-react';
import { Button } from './components/atoms/Button';
import { Header } from './components/organisms/Header';
import { DashboardLayout } from './components/templates/DashboardLayout';
import { StatCard, StatsGrid } from './components/organisms/StatCard';
import { JobCard } from './components/organisms/JobCard';
import { ApplicationCard } from './components/organisms/ApplicationCard';
import { Card, CardHeader, CardContent } from './components/molecules/Card';
import { Badge } from './components/molecules/Badge';
import { ListViewTemplate } from './components/templates/ListViewTemplate';
import { EmptyState } from './components/molecules/EmptyState';
import { Alert } from './components/molecules/Alert';
import DesignTokenEditor from './components/DesignTokenEditor';

export default function App() {
  const [isDark, setIsDark] = useState(false);
  const [currentView, setCurrentView] = useState<'dashboard' | 'jobs' | 'applications' | 'resumes' | 'tokens'>('dashboard');

  const toggleTheme = () => {
    setIsDark(!isDark);
    document.documentElement.classList.toggle('dark');
  };

  // Mock Data
  const stats = [
    {
      icon: Briefcase,
      label: 'Total Applications',
      value: 142,
      change: { value: 12, type: 'increase' as const, label: '+12 this week' },
      color: 'var(--js-primary)'
    },
    {
      icon: Target,
      label: 'Active Jobs',
      value: 38,
      change: { value: 8, type: 'increase' as const, label: '8 interviews scheduled' },
      color: 'var(--js-info)'
    },
    {
      icon: DollarSign,
      label: 'Budget Remaining',
      value: '$340',
      change: { value: -85, type: 'decrease' as const, label: '$85/wk average' },
      color: 'var(--js-success)'
    },
    {
      icon: Calendar,
      label: 'Avg. Response Time',
      value: '4.2d',
      change: { value: -0.8, type: 'increase' as const, label: '0.8d faster than avg' },
      color: 'var(--js-warning)'
    }
  ];

  const recentApplications = [
    {
      company: 'Stripe',
      position: 'Senior Product Manager',
      status: 'interviewing' as const,
      appliedDate: 'Feb 8',
      salary: '$180k-$220k',
      atsScore: 94,
      nextStep: { type: 'Final Interview', date: 'Feb 12' },
      notes: 'Follow up with hiring manager about team structure'
    },
    {
      company: 'Linear',
      position: 'Product Designer',
      status: 'applied' as const,
      appliedDate: 'Feb 6',
      salary: '$150k-$180k',
      atsScore: 87
    },
    {
      company: 'Vercel',
      position: 'Engineering Manager',
      status: 'offered' as const,
      appliedDate: 'Feb 1',
      salary: '$200k-$250k',
      atsScore: 92,
      nextStep: { type: 'Decision Deadline', date: 'Feb 14' }
    }
  ];

  const activeJobs = [
    {
      company: 'Figma',
      title: 'Senior Product Manager',
      location: 'San Francisco, CA',
      salary: '$170k-$210k',
      type: 'full-time' as const,
      postedDate: '2 days ago',
      description: 'Looking for an experienced PM to lead our design systems team. You\'ll work closely with designers and engineers to build the future of collaborative design tools.',
      tags: ['Product Management', 'Design Systems', 'B2B'],
      status: 'active' as const
    },
    {
      company: 'Notion',
      title: 'Product Designer',
      location: 'Remote',
      salary: '$140k-$180k',
      type: 'remote' as const,
      postedDate: '1 week ago',
      description: 'Join our product design team to craft delightful experiences for millions of users. We\'re looking for someone who can think systematically and execute with high attention to detail.',
      tags: ['Product Design', 'Interaction Design', 'Prototyping'],
      status: 'saved' as const
    }
  ];

  const navigationItems = [
    { label: 'Dashboard', active: currentView === 'dashboard', onClick: () => setCurrentView('dashboard') },
    { label: 'Jobs', active: currentView === 'jobs', onClick: () => setCurrentView('jobs'), badge: activeJobs.length },
    { label: 'Applications', active: currentView === 'applications', onClick: () => setCurrentView('applications'), badge: recentApplications.length },
    { label: 'Resumes', active: currentView === 'resumes', onClick: () => setCurrentView('resumes') },
    { label: '🎨 Token Editor', active: currentView === 'tokens', onClick: () => setCurrentView('tokens') }
  ];

  const sidebar = (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--js-space-md)',
      padding: 'var(--js-space-lg)'
    }}>
      <div>
        <h3 style={{
          fontSize: 'var(--js-font-size-caption)',
          fontWeight: 'var(--js-font-weight-semibold)',
          textTransform: 'uppercase',
          letterSpacing: 'var(--js-letter-spacing-uppercase)',
          color: 'var(--js-text)',
          opacity: 0.6,
          marginBottom: 'var(--js-space-sm)'
        }}>
          Quick Stats
        </h3>
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--js-space-sm)',
          fontSize: 'var(--js-font-size-caption)',
          color: 'var(--js-text)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Response Rate</span>
            <span style={{ fontWeight: 'var(--js-font-weight-semibold)' }}>28%</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Interview Rate</span>
            <span style={{ fontWeight: 'var(--js-font-weight-semibold)' }}>12%</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Offer Rate</span>
            <span style={{ fontWeight: 'var(--js-font-weight-semibold)' }}>4%</span>
          </div>
        </div>
      </div>

      <div>
        <h3 style={{
          fontSize: 'var(--js-font-size-caption)',
          fontWeight: 'var(--js-font-weight-semibold)',
          textTransform: 'uppercase',
          letterSpacing: 'var(--js-letter-spacing-uppercase)',
          color: 'var(--js-text)',
          opacity: 0.6,
          marginBottom: 'var(--js-space-sm)'
        }}>
          Application Status
        </h3>
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--js-space-xs)'
        }}>
          <Badge variant="app-applied" style={{ justifyContent: 'space-between' }}>
            Applied <span>87</span>
          </Badge>
          <Badge variant="app-interviewing" style={{ justifyContent: 'space-between' }}>
            Interviewing <span>24</span>
          </Badge>
          <Badge variant="app-offered" style={{ justifyContent: 'space-between' }}>
            Offered <span>6</span>
          </Badge>
          <Badge variant="app-rejected" style={{ justifyContent: 'space-between' }}>
            Rejected <span>20</span>
          </Badge>
        </div>
      </div>
    </div>
  );

  const renderDashboard = () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--js-space-xxl)' }}>
      <div>
        <h1 style={{
          fontSize: 'var(--js-font-size-h1)',
          fontWeight: 'var(--js-font-weight-semibold)',
          lineHeight: 'var(--js-line-height-h1)',
          letterSpacing: 'var(--js-letter-spacing-display)',
          color: 'var(--js-text)',
          margin: '0 0 8px 0'
        }}>
          Dashboard
        </h1>
        <p style={{
          fontSize: 'var(--js-font-size-body-l)',
          lineHeight: 'var(--js-line-height-body-l)',
          color: 'var(--js-text)',
          opacity: 0.7,
          margin: 0
        }}>
          Track your job search progress and manage applications
        </p>
      </div>

      <Alert variant="info" title="Welcome to jSeeker v0.2.1">
        Complete design system with 30 prompts executed: Tokens, Atoms, Molecules, Organisms, Templates, and Full Pages.
        All components follow operational clarity with refined typography (60/40 blend).
      </Alert>

      <StatsGrid stats={stats} />

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--js-space-lg)' }}>
        <Card padding="spacious" elevation={2}>
          <CardHeader
            title="Recent Applications"
            subtitle={`${recentApplications.length} active`}
            action={
              <Button variant="ghost" size="sm" onClick={() => setCurrentView('applications')}>
                View All
              </Button>
            }
          />
          <CardContent>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--js-space-md)' }}>
              {recentApplications.slice(0, 3).map((app, i) => (
                <div key={i} style={{
                  padding: 'var(--js-space-sm)',
                  backgroundColor: 'var(--js-bg)',
                  borderRadius: 'var(--js-border-radius-sm)',
                  border: `var(--js-border-width-thin) solid var(--js-border)`
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 'var(--js-space-xs)' }}>
                    <span style={{
                      fontSize: 'var(--js-font-size-body)',
                      fontWeight: 'var(--js-font-weight-semibold)',
                      color: 'var(--js-text)'
                    }}>
                      {app.position}
                    </span>
                    <Badge variant={`app-${app.status}` as any}>{app.status}</Badge>
                  </div>
                  <div style={{
                    fontSize: 'var(--js-font-size-caption)',
                    color: 'var(--js-text)',
                    opacity: 0.6
                  }}>
                    {app.company} • ATS: {app.atsScore}%
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card padding="spacious" elevation={2}>
          <CardHeader
            title="Active Job Listings"
            subtitle={`${activeJobs.length} jobs saved`}
            action={
              <Button variant="ghost" size="sm" onClick={() => setCurrentView('jobs')}>
                View All
              </Button>
            }
          />
          <CardContent>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--js-space-md)' }}>
              {activeJobs.map((job, i) => (
                <div key={i} style={{
                  padding: 'var(--js-space-sm)',
                  backgroundColor: 'var(--js-bg)',
                  borderRadius: 'var(--js-border-radius-sm)',
                  border: `var(--js-border-width-thin) solid var(--js-border)`
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 'var(--js-space-xs)' }}>
                    <span style={{
                      fontSize: 'var(--js-font-size-body)',
                      fontWeight: 'var(--js-font-weight-semibold)',
                      color: 'var(--js-text)'
                    }}>
                      {job.title}
                    </span>
                    <Badge variant={`job-${job.status}` as any}>{job.status}</Badge>
                  </div>
                  <div style={{
                    fontSize: 'var(--js-font-size-caption)',
                    color: 'var(--js-text)',
                    opacity: 0.6,
                    display: 'flex',
                    alignItems: 'center',
                    gap: 'var(--js-space-sm)'
                  }}>
                    <span>{job.company}</span>
                    <span>•</span>
                    <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <MapPin size={12} />
                      {job.location}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );

  const renderJobs = () => (
    <ListViewTemplate
      title="Job Listings"
      subtitle="Browse and save job opportunities"
      actions={
        <Button variant="primary" iconLeft={<Plus size={20} />}>
          Add Job
        </Button>
      }
      searchFilter={{
        searchPlaceholder: 'Search jobs by title, company, or keywords...',
        filters: [
          {
            key: 'location',
            label: 'Location',
            type: 'select',
            options: [
              { value: 'remote', label: 'Remote' },
              { value: 'sf', label: 'San Francisco' },
              { value: 'nyc', label: 'New York' }
            ]
          },
          {
            key: 'type',
            label: 'Job Type',
            type: 'select',
            options: [
              { value: 'full-time', label: 'Full Time' },
              { value: 'part-time', label: 'Part Time' },
              { value: 'contract', label: 'Contract' }
            ]
          }
        ]
      }}
    >
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(400px, 1fr))', gap: 'var(--js-space-lg)' }}>
        {activeJobs.map((job, i) => (
          <JobCard key={i} {...job} />
        ))}
      </div>
    </ListViewTemplate>
  );

  const renderApplications = () => (
    <ListViewTemplate
      title="Applications"
      subtitle={`Tracking ${recentApplications.length} applications`}
      actions={
        <Button variant="primary" iconLeft={<Plus size={20} />}>
          Add Application
        </Button>
      }
      searchFilter={{
        searchPlaceholder: 'Search applications...',
        filters: [
          {
            key: 'status',
            label: 'Status',
            type: 'select',
            options: [
              { value: 'applied', label: 'Applied' },
              { value: 'interviewing', label: 'Interviewing' },
              { value: 'offered', label: 'Offered' },
              { value: 'rejected', label: 'Rejected' }
            ]
          }
        ]
      }}
    >
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--js-space-lg)' }}>
        {recentApplications.map((app, i) => (
          <ApplicationCard key={i} {...app} />
        ))}
      </div>
    </ListViewTemplate>
  );

  const renderResumes = () => (
    <ListViewTemplate
      title="Resumes"
      subtitle="Manage your resume versions"
      actions={
        <Button variant="primary" iconLeft={<Plus size={20} />}>
          Create Resume
        </Button>
      }
      isEmpty
      emptyState={
        <EmptyState
          icon={FileText}
          title="No resumes yet"
          description="Create your first tailored resume to start applying to jobs with optimized ATS scores"
          action={{
            label: 'Create Resume',
            onClick: () => console.log('Create resume'),
            icon: <Plus size={20} />
          }}
        />
      }
    />
  );

  // Render Token Editor without DashboardLayout
  if (currentView === 'tokens') {
    return <DesignTokenEditor />;
  }

  return (
    <DashboardLayout
      header={
        <Header
          title="jSeeker v0.2.1"
          navigation={navigationItems}
          notifications={3}
          userMenu={{
            name: 'John Doe',
            email: 'john@example.com'
          }}
          onNotificationClick={() => console.log('Notifications')}
          onUserClick={() => console.log('User menu')}
        />
      }
      sidebar={sidebar}
    >
      {currentView === 'dashboard' && renderDashboard()}
      {currentView === 'jobs' && renderJobs()}
      {currentView === 'applications' && renderApplications()}
      {currentView === 'resumes' && renderResumes()}
    </DashboardLayout>
  );
}
