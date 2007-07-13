#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Finance
%define		pnam	Quote
Summary:	Get stock and mutual fund quotes from various exchanges
Name:		perl-Finance-Quote
Version:	1.13
Release:	1
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Finance/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Finance-Quote/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Get stock and mutual fund quotes from various exchange.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Finance/*.pm
%dir %{perl_vendorlib}/Finance/Quote
%{perl_vendorlib}/Finance/Quote/*.pm
%dir %{perl_vendorlib}/Finance/Quote/Yahoo
%{perl_vendorlib}/Finance/Quote/Yahoo/*.pm
%{_mandir}/man3/*
