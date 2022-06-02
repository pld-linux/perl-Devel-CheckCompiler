#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	CheckCompiler
Summary:	Devel::CheckCompiler - check the compiler's availability
Summary(pl.UTF-8):	Devel::CheckCompiler - sprawdzanie dostępności kompilatora
Name:		perl-Devel-CheckCompiler
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fcd7ba5891f9f4a0fb61b79fcda89e75
URL:		https://metacpan.org/dist/Devel-CheckCompiler
BuildRequires:	perl-Module-Build-Tiny >= 0.035
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::CheckCompiler is checker for compiler's availability.

%description -l pl.UTF-8
Devel::CheckCompiler to moduł do sprawdzania dostępności kompilatora.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Devel/AssertC99.pm
%{perl_vendorlib}/Devel/CheckCompiler.pm
%{_mandir}/man3/Devel::AssertC99.3pm*
%{_mandir}/man3/Devel::CheckCompiler.3pm*
