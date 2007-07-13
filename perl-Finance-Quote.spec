#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Finance
%define		pnam	Quote
Summary:	Finance::Quote - Get stock and mutual fund quotes from various exchanges
Name:		perl-Finance-Quote
Version:	1.13
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Finance/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Finance-Quote/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module gets stock quotes from various internet sources, including
Yahoo! Finance, Fidelity Investments, and the Australian Stock Exchange.
There are two methods of using this module -- a functional interface
that is depreciated, and an object-orientated method that provides
greater flexibility and stability.

With the exception of straight currency exchange rates, all information
is returned as a two-dimensional hash (or a reference to such a hash,
if called in a scalar context).  For example:

    %info = $q->fetch("australia","CML");
    print "The price of CML is ".$info{"CML","price"};

The first part of the hash (eg, "CML") is referred to as the stock.
The second part (in this case, "price") is referred to as the label.

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
