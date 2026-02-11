// jSeeker v0.2.1 Design System - Component Index
// Complete export manifest for all 31 components

// ============================================
// ATOMS (Prompts #6-12) - 7 Components
// ============================================
export { Button } from './components/atoms/Button';
export type { ButtonProps } from './components/atoms/Button';

export { Input } from './components/atoms/Input';
export type { InputProps } from './components/atoms/Input';

export { Checkbox } from './components/atoms/Checkbox';
export type { CheckboxProps } from './components/atoms/Checkbox';

export { Radio } from './components/atoms/Radio';
export type { RadioProps } from './components/atoms/Radio';

export { Select } from './components/atoms/Select';
export type { SelectProps } from './components/atoms/Select';

export { Textarea } from './components/atoms/Textarea';
export type { TextareaProps } from './components/atoms/Textarea';

export { Toggle } from './components/atoms/Toggle';
export type { ToggleProps } from './components/atoms/Toggle';

// ============================================
// MOLECULES (Prompts #13-18) - 6 Components
// ============================================
export { FormField } from './components/molecules/FormField';
export type { FormFieldProps } from './components/molecules/FormField';

export { Card, CardHeader, CardContent } from './components/molecules/Card';
export type { CardProps, CardHeaderProps, CardContentProps } from './components/molecules/Card';

export { Badge } from './components/molecules/Badge';
export type { BadgeProps, BadgeVariant } from './components/molecules/Badge';

export { Alert } from './components/molecules/Alert';
export type { AlertProps, AlertVariant } from './components/molecules/Alert';

export { Modal, ConfirmModal } from './components/molecules/Modal';
export type { ModalProps, ConfirmModalProps } from './components/molecules/Modal';

export { EmptyState } from './components/molecules/EmptyState';
export type { EmptyStateProps } from './components/molecules/EmptyState';

// ============================================
// ORGANISMS (Prompts #19-25) - 7 Components
// ============================================
export { DataTable } from './components/organisms/DataTable';
export type { DataTableProps, Column } from './components/organisms/DataTable';

export { JobCard } from './components/organisms/JobCard';
export type { JobCardProps } from './components/organisms/JobCard';

export { ApplicationCard } from './components/organisms/ApplicationCard';
export type { ApplicationCardProps, ApplicationStatus } from './components/organisms/ApplicationCard';

export { StatCard, StatsGrid } from './components/organisms/StatCard';
export type { StatCardProps, StatsGridProps } from './components/organisms/StatCard';

export { SearchFilterBar } from './components/organisms/SearchFilterBar';
export type { SearchFilterBarProps, FilterOption } from './components/organisms/SearchFilterBar';

export { ResumeBuilderForm } from './components/organisms/ResumeBuilderForm';
export type { ResumeBuilderFormProps, ResumeData } from './components/organisms/ResumeBuilderForm';

export { Header } from './components/organisms/Header';
export type { HeaderProps, NavigationItem } from './components/organisms/Header';

// ============================================
// TEMPLATES (Prompts #26-29) - 4 Components
// ============================================
export { DashboardLayout } from './components/templates/DashboardLayout';
export type { DashboardLayoutProps } from './components/templates/DashboardLayout';

export { ListViewTemplate } from './components/templates/ListViewTemplate';
export type { ListViewTemplateProps } from './components/templates/ListViewTemplate';

export { DetailViewTemplate } from './components/templates/DetailViewTemplate';
export type { DetailViewTemplateProps } from './components/templates/DetailViewTemplate';

export { FormTemplate } from './components/templates/FormTemplate';
export type { FormTemplateProps, FormSection } from './components/templates/FormTemplate';

// ============================================
// USAGE EXAMPLES
// ============================================

/*
// Import individual components:
import { Button, Input, Card } from './index';

// Import with types:
import { Button, type ButtonProps } from './index';

// Import from specific layers:
import { Button } from './components/atoms/Button';
import { Card } from './components/molecules/Card';
import { Header } from './components/organisms/Header';
import { DashboardLayout } from './components/templates/DashboardLayout';

// Build complete pages:
import {
  DashboardLayout,
  Header,
  StatCard,
  ApplicationCard,
  JobCard
} from './index';

function MyDashboard() {
  return (
    <DashboardLayout header={<Header />}>
      <StatCard {...statsData} />
      <ApplicationCard {...appData} />
      <JobCard {...jobData} />
    </DashboardLayout>
  );
}
*/
